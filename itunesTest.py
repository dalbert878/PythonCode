import unittest
from unittest.mock import patch, MagicMock
import sys
import requests
from io import StringIO

# Assuming the script is named `itunes.py` and contains the `main()` function
from itunes import main

class TestItunesSearch(unittest.TestCase):

    @patch('itunes.requests.get')
    def test_successful_response(self, mock_get):
        """ Test with a successful response from the iTunes API. """

        # Mock the API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {"trackName": "Track 1"},
                {"trackName": "Track 2"}
            ]
        }
        mock_get.return_value = mock_response

        # Simulate the command-line argument
        sys.argv = ['itunes.py', 'Beatles']

        # Capture print output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue().strip().split('\n')
            self.assertEqual(output, ['Track 1', 'Track 2'])

    @patch('itunes.requests.get')
    def test_no_results(self, mock_get):
        """ Test with no results in the response. """

        # Mock an empty response
        mock_response = MagicMock()
        mock_response.json.return_value = {"results": []}
        mock_get.return_value = mock_response

        # Simulate the command-line argument
        sys.argv = ['itunes.py', 'Beatles']

        # Capture print output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    @patch('itunes.requests.get')
    def test_request_failure(self, mock_get):
        """ Test the main() function when the HTTP request fails. """

        # Simulate a request failure
        mock_get.side_effect = requests.RequestException("Request failed")

        # Simulate the command-line argument
        sys.argv = ['itunes.py', 'Beatles']

        # Capture stdout and stderr
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(SystemExit):
                main()

            output = fake_out.getvalue().strip()
            self.assertIn("HTTP Request failed: Request failed", output)

if __name__ == '__main__':
    unittest.main()
