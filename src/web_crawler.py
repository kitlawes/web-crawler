import urllib2
import os

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
        assets = []
        asset_extensions = self.get_asset_extensions()
        for same_subdomain_address in same_subdomain_addresses:
            for asset_extension in asset_extensions:
                if same_subdomain_address.endswith(asset_extension):
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
            if is_web_page:
                web_pages.append(same_subdomain_address)
        return web_pages

    def get_asset_extensions(self):
        asset_extensions = []
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'asset_extensions.txt')
        with open(file_path, 'r') as file:
            for line in file:
                asset_extensions.append(line.rstrip('\n'))
        return asset_extensions