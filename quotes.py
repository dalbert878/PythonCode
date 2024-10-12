import requests
import sys
import json

def main():
    """
    Main function to search for songs on iTunes based on a search term provided via command line arguments.
    Prints the track names of the search results.
    """

    url = "https://zenquotes.io/api/random/?option1=value&option2=value"

    # Perform the HTTP GET request to the iTunes Search API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
        sys.exit(1)

    # Parse the JSON response
    data = response.json()

# No need for loop if you're accessing the first item directly
    quote = (data[0]["q"])
    auth = (data[0]["a"])



if __name__ == "__main__":
    main()
