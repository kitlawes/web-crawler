import unittest
from src.web_crawler import WebCrawler

class WebCrawlerSpec(unittest.TestCase):

    def test_get_html(self):
        expected_html = self.get_file_contents("quotes_to_scrape.html")
        web_crawler = WebCrawler()
        actual_html = web_crawler.get_html("http://quotes.toscrape.com/")
        self.assertEqual(expected_html, actual_html)

    def test_get_links(self):
        expected_links = self.get_file_contents("quotes_to_scrape_links.txt")
        web_crawler = WebCrawler()
        quotes_to_scrape_html = self.get_file_contents("quotes_to_scrape.html")
        actual_links = web_crawler.get_links(quotes_to_scrape_html)
        self.assertEqual(expected_links, actual_links)

    def get_file_contents(self, file_name):
        file_contents = []
        with open(file_name, 'r') as file:
            for line in file:
                file_contents.append(line.rstrip('\n'))
        return file_contents