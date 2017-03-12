import urllib2

class WebCrawler:

    def get_html(self, url):
        html = []
        for line in urllib2.urlopen(url):
            html.append(line.rstrip('\n'))
        return html

    def get_links(self, html):
        links = []
        for line in html:
            if "href=\"" in line:
                start = line.index("href=\"") + len("href=\"")
                end = line.index("\"", start)
                links.append(line[start: end])
        return links

    def get_same_subdomain_addresses_from_links(self, subdomain, links):
        same_subdomain_addresses = []
        for link in links:
            if link.startswith("/"):
                same_subdomain_addresses.append(subdomain.rstrip('/') + link)
            if link.startswith(subdomain):
                same_subdomain_addresses.append(link)
        return same_subdomain_addresses