import unittest
from html_parser import HtmlParser
from file_util import FileUtil

class TestHtmlParser(unittest.TestCase):

    def test_get_links(self):
        """
        Tests get_links method
        """
        file_util = FileUtil()
        expected_links = file_util.get_file_contents("links_test_data.txt")
        html_parser = HtmlParser()
        html_test_data = file_util.get_file_contents("html_test_data.html")
        actual_links = html_parser.get_links(html_test_data)
        self.assertEqual(expected_links, actual_links)

    def test_get_same_hostname_urls(self):
        """
        Tests get_same_hostname_urls method
        """
        file_util = FileUtil()
        expected_same_hostname_urls = file_util.get_file_contents("same_hostname_urls_test_data.txt")
        html_parser = HtmlParser()
        hostname = "http://www.domain.com/"
        links = file_util.get_file_contents("links_test_data.txt")
        actual_same_hostname_urls = html_parser.get_same_hostname_urls(hostname, links)
        self.assertEqual(expected_same_hostname_urls, actual_same_hostname_urls)

    def test_get_assets(self):
        """
        Tests get_file_contents method
        """
        file_util = FileUtil()
        expected_assets = file_util.get_file_contents("assets_test_data.txt")
        html_parser = HtmlParser()
        urls = file_util.get_file_contents("same_hostname_urls_test_data.txt")
        actual_assets = html_parser.get_assets(urls)
        self.assertEqual(expected_assets, actual_assets)

    def test_get_web_pages(self):
        """
        Tests get_web_pages method
        """
        file_util = FileUtil()
        expected_web_pages = file_util.get_file_contents("web_pages_test_data.txt")
        html_parser = HtmlParser()
        same_hostname_urls = file_util.get_file_contents("same_hostname_urls_test_data.txt")
        actual_web_pages = html_parser.get_web_pages(same_hostname_urls)
        self.assertEqual(expected_web_pages, actual_web_pages)