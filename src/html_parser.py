import os
from url_util import UrlUtil

class HtmlParser:

    def __init__(self):
        self.url_util = UrlUtil()

    def get_links(self, html):
        """
        Extracts and returns the links in the parameter HTML
        """
        links = []
        link_prefixes = ["href=\"", "src=\""]
        for line in html:
            link_found = True
            # Each iteration of this loop finds a link in the line.
            while link_found:
                link_found = False
                start = len(line)
                end = len(line)
                # The next link in the line could have any link_prefix.
                for link_prefix in link_prefixes:
                    if link_prefix in line:
                        link_found = True
                        link_prefix_start = line.index(link_prefix) + len(link_prefix)
                        link_prefix_end = line.index("\"", link_prefix_start)
                        # If the next link in the line prefixed by link_prefix is the closest to the start of line so far
                        if link_prefix_start < start:
                            start = link_prefix_start
                            end = link_prefix_end
                if link_found:
                    links.append(line[start:end])
                    line = line[end:]
        return links

    def get_same_hostname_urls(self, hostname, links):
        """
        Returns the links from the parameter links that have the same hostname as the parameter hostname
        The links returned are converted into absolute urls.
        """

        hostname = self.url_util.normalise_url(hostname)
        
        same_hostname_urls = []
        for link in links:
            
            # Normalise link
            if link.endswith("/"):
                link = link.rstrip("/")
            if link.startswith("https://"):
                link = link.lstrip("https://")
                link = "http://" + link
            if link.startswith("//"):
                link = "http:" + link

            if link.startswith(hostname):
                # Link starts with hostname.
                same_hostname_urls.append(link)
            elif not link.startswith("http://"):
                # Link is relative, so prefix the link with hostname
                if link != "" and not link.startswith("/"):
                    link = "/" + link
                same_hostname_urls.append(hostname + link)
                
        return same_hostname_urls

    def get_assets(self, urls):
        """
        Returns the urls from the parameter urls that refer to assets
        """
        assets = []
        asset_extensions = self.get_asset_extensions()
        for url in urls:
            for asset_extension in asset_extensions:
                if url.endswith(asset_extension):
                    # Assets should be unique.
                    if url not in assets:
                        assets.append(url)
                    break
        return assets

    def get_web_pages(self, urls):
        """
        Returns the urls from the parameter urls that refer to web pages
        """
        web_pages = []
        asset_extensions = self.get_asset_extensions()
        for url in urls:
            is_web_page = True
            for asset_extension in asset_extensions:
                if url.endswith(asset_extension):
                    is_web_page = False
                    break
            # Web pages should be unique.
            if is_web_page and url not in web_pages:
                web_pages.append(url)
        return web_pages

    def get_asset_extensions(self):
        """
        Returns file extensions for assets
        """
        asset_extensions = []
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'asset_extensions.txt')
        with open(file_path, 'r') as file:
            for line in file:
                asset_extensions.append(line.rstrip('\n'))
        return asset_extensions