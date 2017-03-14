import sys
sys.path.append("../src/")

import unittest
from test_web_crawler import TestWebCrawler
from test_html_requester import TestHtmlRequester
from test_html_parser import TestHtmlParser
from test_url_util import TestUrlUtil

if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    suite = test_loader.loadTestsFromTestCase(TestWebCrawler)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHtmlRequester)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHtmlParser)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUrlUtil)
    unittest.TextTestRunner(verbosity=2).run(suite)