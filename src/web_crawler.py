import urllib2

class WebCrawler:

    def get_html(self, url):
        html = []
        for line in urllib2.urlopen(url):
            html.append(line)
        return html