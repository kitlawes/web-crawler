import unittest
from url_util import UrlUtil

class TestUrlUtil(unittest.TestCase):

    def test_get_hostname(self):
        """
        Tests get_hostname method
        """

        url_util = UrlUtil()

        expected_result = "http://www.domain.com"
        actual_result = url_util.get_hostname("http://www.domain.com")
        self.assertEqual(expected_result, actual_result)

        expected_result = "http://www.domain.com"
        actual_result = url_util.get_hostname("http://www.domain.com/page")
        self.assertEqual(expected_result, actual_result)

    def test_normalise_url(self):
        """
        Tests normalise_url method
        """

        url_util = UrlUtil()
        
        expected_result = "http://www.domain.com"
        actual_result = url_util.normalise_url("http://www.domain.com")
        self.assertEqual(expected_result, actual_result)

        expected_result = "http://www.domain.com/page"
        actual_result = url_util.normalise_url("http://www.domain.com/page")
        self.assertEqual(expected_result, actual_result)

        expected_result = "http://www.domain.com"
        actual_result = url_util.normalise_url("https://www.domain.com")
        self.assertEqual(expected_result, actual_result)

        expected_result = "http://www.domain.com"
        actual_result = url_util.normalise_url("www.domain.com")
        self.assertEqual(expected_result, actual_result)

        expected_result = "http://www.domain.com"
        actual_result = url_util.normalise_url("domain.com")
        self.assertEqual(expected_result, actual_result)

        expected_result = "http://www.domain.com"
        actual_result = url_util.normalise_url("http://www.domain.com/")
        self.assertEqual(expected_result, actual_result)