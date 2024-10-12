import unittest
from unittest.mock import patch, Mock
import requests  # Make sure to import the requests module
from webScrape import fetch_articles  # Replace 'your_module' with the actual name of your Python file without the .py extension

class TestFetchArticles(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_articles_success(self, mock_get):
        # Mock a successful response with sample HTML content
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '''
            <html>
                <body>
                    <a class="optimize-track" href="http://example.com/article1">Article 1</a>
                    <a class="optimize-track" href="http://example.com/article2">Article 2</a>
                </body>
            </html>
        '''
        mock_get.return_value = mock_response

        url = "https://www.inquirer.net/"
        headers = {'User-Agent': 'test-agent'}

        # Call the function and check the result
        result = fetch_articles(url, headers)
        expected_result = [
            "1. Article 1\nLink: http://example.com/article1\n",
            "2. Article 2\nLink: http://example.com/article2\n"
        ]
        self.assertEqual(result, expected_result)

    @patch('requests.get')
    def test_fetch_articles_no_titles(self, mock_get):
        # Mock a successful response with no titles
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '''
            <html>
                <body>
                </body>
            </html>
        '''
        mock_get.return_value = mock_response

        url = "https://www.inquirer.net/"
        headers = {'User-Agent': 'test-agent'}

        # Call the function and check the result
        result = fetch_articles(url, headers)
        expected_result = ["No articles found. Check if the class names have changed."]
        self.assertEqual(result, expected_result)

    @patch('requests.get')
    def test_fetch_articles_http_error(self, mock_get):
        # Mock an HTTP error (e.g., 404 Not Found)
        mock_get.side_effect = requests.exceptions.HTTPError("404 Client Error: Not Found for url")

        url = "https://www.inquirer.net/"
        headers = {'User-Agent': 'test-agent'}

        # Call the function and check the result
        result = fetch_articles(url, headers)
        expected_result = ["Failed to fetch page: 404 Client Error: Not Found for url"]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
