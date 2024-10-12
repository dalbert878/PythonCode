import requests
from bs4 import BeautifulSoup

def fetch_articles(url, headers):
    try:
        # Send a GET request to the website and raise error for unsuccessful status codes
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError if the status code is not 200

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all titles on the page
        titles = soup.find_all('a', class_='optimize-track')

        # Return the formatted results or a message if no titles found
        return [
            f"{idx}. {title.get_text()}\nLink: {title.get('href')}\n"
            for idx, title in enumerate(titles, 1)
        ] or ["No articles found. Check if the class names have changed."]

    except requests.exceptions.RequestException as e:
        return [f"Failed to fetch page: {e}"]

def main():
    # URL of the website you want to scrape
    url = "https://www.inquirer.net/"

    # Add headers to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Fetch and print articles
    for article in fetch_articles(url, headers):
        print(article)

# The standard boilerplate to call the main() function
if __name__ == "__main__":
    main()
