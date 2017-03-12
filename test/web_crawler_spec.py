import unittest
from src.web_crawler import WebCrawler
import os

class WebCrawlerSpec(unittest.TestCase):

    def test_get_html(self):
        expected_html = self.get_file_contents("example.html")
        web_crawler = WebCrawler()
        actual_html = web_crawler.get_html("http://example.org")
        self.assertEqual(expected_html, actual_html)

    def test_get_links(self):
        expected_links = self.get_file_contents("links_test_data.txt")
        web_crawler = WebCrawler()
        quotes_to_scrape_html = self.get_file_contents("html_test_data.html")
        actual_links = web_crawler.get_links(quotes_to_scrape_html)
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

    def get_file_contents(self, file_name):
        file_contents = []
        file_path = os.path.join(os.path.dirname(__file__), 'resources', file_name)
        with open(file_path, 'r') as file:
            for line in file:
                file_contents.append(line.rstrip('\n'))
        return file_contents