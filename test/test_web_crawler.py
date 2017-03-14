import unittest
from web_crawler import WebCrawler
from file_util import FileUtil

class TestWebCrawler(unittest.TestCase):
    
    def test_crawl(self):
        """
        Tests crawl method
        The get_html method of the html_requester class is mocked to return the contents of html_test_data.html.
        This mocking allows for inputting test html data without having to host it online.
        """
        file_util = FileUtil()
        expected_result = file_util.get_file_contents("crawl_test_data.txt")
        web_crawler = WebCrawler()
        web_crawler.html_requester.get_html = lambda url: self.mock_get_html(url)
        actual_result = web_crawler.crawl("http://www.domain.com")
        self.assertEqual(expected_result, actual_result)

    def mock_get_html(self, url):
        """
        Mocks the get_html method of the html_requester class to return the contents of html_test_data.html
        This mocking allows for inputting test html data without having to host it online.
        """
        if url == "http://www.domain.com":
            file_util = FileUtil()
            html_test_data = file_util.get_file_contents("html_test_data.html")
            return html_test_data
        else:
            return ""