import unittest
from src.web_crawler import WebCrawler
import os

class WebCrawlerSpec(unittest.TestCase):

    def get_html(self, url):
        if url == "http://www.domain.com":
            html_test_data = self.get_file_contents("html_test_data.html")
            return html_test_data
        else:
            return ""

    def test_crawl(self):
        expected_result = self.get_file_contents("crawl_test_data.txt")
        web_crawler = WebCrawler()
        web_crawler.get_html = lambda url: self.get_html(url)
        actual_result = web_crawler.crawl("http://www.domain.com")
        self.assertEqual(expected_result, actual_result)

    def test_get_html(self):
        expected_html = self.get_file_contents("example.html")
        web_crawler = WebCrawler()
        actual_html = web_crawler.get_html("http://example.org")
        self.assertEqual(expected_html, actual_html)

    def test_get_links(self):
        expected_links = self.get_file_contents("links_test_data.txt")
        web_crawler = WebCrawler()
        html_test_data = self.get_file_contents("html_test_data.html")
        actual_links = web_crawler.get_links(html_test_data)
        self.assertEqual(expected_links, actual_links)

    def test_get_same_subdomain_addresses(self):
        expected_same_subdomain_addresses = self.get_file_contents("same_subdomain_addresses_test_data.txt")
        web_crawler = WebCrawler()
        subdomain = "http://www.domain.com/"
        quotes_to_scrape_links = self.get_file_contents("links_test_data.txt")
        actual_same_subdomain_addresses = web_crawler.get_same_subdomain_addresses(subdomain, quotes_to_scrape_links)
        self.assertEqual(expected_same_subdomain_addresses, actual_same_subdomain_addresses)

    def test_get_assets(self):
        expected_assets = self.get_file_contents("assets_test_data.txt")
        web_crawler = WebCrawler()
        same_subdomain_addresses = self.get_file_contents("same_subdomain_addresses_test_data.txt")
        actual_assets = web_crawler.get_assets(same_subdomain_addresses)
        self.assertEqual(expected_assets, actual_assets)

    def test_get_web_pages(self):
        expected_web_pages = self.get_file_contents("web_pages_test_data.txt")
        web_crawler = WebCrawler()
        same_subdomain_addresses = self.get_file_contents("same_subdomain_addresses_test_data.txt")
        actual_web_pages = web_crawler.get_web_pages(same_subdomain_addresses)
        self.assertEqual(expected_web_pages, actual_web_pages)

    def get_file_contents(self, file_name):
        file_contents = []
        file_path = os.path.join(os.path.dirname(__file__), 'resources', file_name)
        with open(file_path, 'r') as file:
            for line in file:
                file_contents.append(line.rstrip('\n'))
        return file_contents