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
            if "src=\"" in line:
                start = line.index("src=\"") + len("src=\"")
                end = line.index("\"", start)
                links.append(line[start: end])
        return links

    def get_same_subdomain_addresses(self, subdomain, links):
        if not subdomain.startswith("http://"):
            subdomain = "http://" + subdomain
        if subdomain.endswith("/"):
            subdomain = subdomain.rstrip("/")
        same_subdomain_addresses = []
        for link in links:
            if link.endswith("/"):
                link = link.rstrip("/")
            if link.startswith(subdomain):
                same_subdomain_addresses.append(link)
            elif not link.startswith("http://"):
                if link != "" and not link.startswith("/"):
                    link = "/" + link
                same_subdomain_addresses.append(subdomain + link)
        return same_subdomain_addresses

    def get_assets(self, same_subdomain_addresses):
        pass