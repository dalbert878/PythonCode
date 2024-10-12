import requests
import sys
import json

def main():
    """
    Main function to search for songs on iTunes based on a search term provided via command line arguments.
    Prints the track names of the search results.
    """
    # Ensure exactly one command line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python itunes.py <search_term>")
        sys.exit(1)

    band_name = sys.argv[1]
    url = f"https://itunes.apple.com/search?entity=song&term={band_name}"

    # Perform the HTTP GET request to the iTunes Search API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
        sys.exit(1)

    # Parse the JSON response
    data = response.json()

    json_string = json.dumps(data, indent=4)
    with open(str(band_name + '.json'), 'w') as file:
        file.write(json_string)

    # Print track names from the search results
    for result in data.get("results", []):
        print(result.get("trackName", "No track name"))

if __name__ == "__main__":
    main()
