import unittest
from src.web_crawler import WebCrawler

class WebCrawlerSpec(unittest.TestCase):
    
    def test_get_html(self):
        
        expected_html = []
        with open("quotes_to_scrape.html", 'r') as file:
            for line in file:
                expected_html.append(line)

        web_crawler = WebCrawler()
        actual_html = web_crawler.get_html("http://quotes.toscrape.com/")

        self.assertEqual(expected_html, actual_html)