import json
from url_util import UrlUtil
from html_requester import HtmlRequester
from html_parser import HtmlParser
import sys

class WebCrawler:

    def __init__(self):
         self.url_util = UrlUtil()
         self.html_requester = HtmlRequester()
         self.html_parser = HtmlParser()

    def crawl(self, url):
        """
        Returns the URLs reachable from the parameter URL
        The assets of each URL are also returned.
        Only URLs with the same hostname including subdomain as the parameter URL are returned.
        """

        url = self.url_util.normalise_url(url)
        hostname = self.url_util.get_hostname(url)

        urlsToVisit = [url]
        urlsVisted = []
        output = []
        # Each iteration of this loop processes the next URL to visit.
        while (len(urlsToVisit) > 0):
            
            url = urlsToVisit.pop(0)
            urlsVisted.append(url)

            html = self.html_requester.get_html(url)
            links = self.html_parser.get_links(html)
            same_hostname_urls = self.html_parser.get_same_hostname_urls(hostname, links)
            assets = self.html_parser.get_assets(same_hostname_urls)
            web_pages = self.html_parser.get_web_pages(same_hostname_urls)
    
            output.append({"url":url,"assets":assets})
            print json.dumps({"url":url,"assets":assets}, indent=4)
    
            for web_page in web_pages:
                # Do not visit a page more than once
                if not web_page in urlsToVisit and web_page not in urlsVisted:
                    urlsToVisit.append(web_page)
        
        return json.dumps(output, indent=4).splitlines()

if __name__ == '__main__':
    web_crawler = WebCrawler()
    result = web_crawler.crawl(sys.argv[1])