import urllib2
import os
import json

class WebCrawler:
    
    def crawl(self, url):

        if url.startswith("https://"):
            url = url.lstrip("https://")
        if not url.startswith("http://"):
            url = "http://" + url
        if not url.startswith("http://www."):
            url = "http://www." + url.lstrip("http://")
        if url.endswith("/"):
            url = url.rstrip("/")
        
        subdomain = url
        end = subdomain.find("/", len("http://"))
        if end != -1:
            subdomain = subdomain[:end]

        urlsToVisit = [url]
        urlsVisted = []
        output = []
        while (len(urlsToVisit) > 0):
            
            url = urlsToVisit.pop(0)
            urlsVisted.append(url)

            html = self.get_html(url)
            links = self.get_links(html)
            same_subdomain_addresses = self.get_same_subdomain_addresses(subdomain, links)
            assets = self.get_assets(same_subdomain_addresses)
            web_pages = self.get_web_pages(same_subdomain_addresses)
    
            output.append({"url":url,"assets":assets})
            print json.dumps({"url":url,"assets":assets}, indent=4)
    
            for web_page in web_pages:
                if not web_page in urlsToVisit and web_page not in urlsVisted:
                    urlsToVisit.append(web_page)
        
        return json.dumps(output, indent=4).splitlines()

    def get_html(self, url):
        html = []
        try:
            for line in urllib2.urlopen(url):
                html.append(line.rstrip('\n'))
        except urllib2.HTTPError as err:
            pass
        return html

    def get_links(self, html):
        links = []
        attributes = ["href=\"", "src=\""]
        for line in html:
            link_found = True
            while link_found:
                link_found = False
                start = len(line)
                end = len(line)
                for attribute in attributes:
                    if attribute in line:
                        link_found = True
                        attribute_start = line.index(attribute) + len(attribute)
                        attribute_end = line.index("\"", attribute_start)
                        if attribute_start < start:
                            start = attribute_start
                            end = attribute_end
                if link_found:
                    links.append(line[start:end])
                    line = line[end:]
        return links

    def get_same_subdomain_addresses(self, subdomain, links):
        
        if subdomain.startswith("https://"):
            subdomain =  subdomain.lstrip("https://")
        if not subdomain.startswith("http://"):
            subdomain = "http://" + subdomain
        if not subdomain.startswith("http://www."):
            subdomain = "http://www." + subdomain.lstrip("http://")
        if subdomain.endswith("/"):
            subdomain = subdomain.rstrip("/")
            
        same_subdomain_addresses = []
        for link in links:
            if link.endswith("/"):
                link = link.rstrip("/")
            if link.startswith("https://"):
                link = link.lstrip("https://")
                link = "http://" + link
            if link.startswith("//"):
                link = "http:" + link
            if link.startswith(subdomain):
                same_subdomain_addresses.append(link)
            elif not link.startswith("http://"):
                if link != "" and not link.startswith("/"):
                    link = "/" + link
                same_subdomain_addresses.append(subdomain + link)
        return same_subdomain_addresses

    def get_assets(self, same_subdomain_addresses):
        assets = []
        asset_extensions = self.get_asset_extensions()
        for same_subdomain_address in same_subdomain_addresses:
            for asset_extension in asset_extensions:
                if same_subdomain_address.endswith(asset_extension):
                    if  same_subdomain_address not in assets:
                        assets.append(same_subdomain_address)
                    break
        return assets

    def get_web_pages(self, same_subdomain_addresses):
        web_pages = []
        asset_extensions = self.get_asset_extensions()
        for same_subdomain_address in same_subdomain_addresses:
            is_web_page = True
            for asset_extension in asset_extensions:
                if same_subdomain_address.endswith(asset_extension):
                    is_web_page = False
                    break
            if is_web_page and same_subdomain_address not in web_pages:
                web_pages.append(same_subdomain_address)
        return web_pages

    def get_asset_extensions(self):
        asset_extensions = []
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'asset_extensions.txt')
        with open(file_path, 'r') as file:
            for line in file:
                asset_extensions.append(line.rstrip('\n'))
        return asset_extensions

if __name__ == '__main__':
    web_crawler = WebCrawler()
    result = web_crawler.crawl("youtube.com")