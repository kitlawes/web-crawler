import unittest
from html_requester import HtmlRequester
from file_util import FileUtil

class TestHtmlRequester(unittest.TestCase):

    def test_get_html(self):
        """
        Tests get_html method
        """
        file_util = FileUtil()
        expected_html = file_util.get_file_contents("example.html")
        html_requester = HtmlRequester()
        actual_html = html_requester.get_html("http://example.org")
        self.assertEqual(expected_html, actual_html)