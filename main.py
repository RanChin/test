import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Replace 'your-selector' with the appropriate CSS selector for the data you want to scrape
        # For example, if you want to scrape all the text from <p> elements, you can use 'p' as the selector
        elements = soup.select('a')

        # Process and print the scraped data
        for element in elements:
            print(f"{element}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    # Replace 'your-url' with the URL of the webpage you want to scrape
    url_to_scrape = 'https://www.patreon.com/gunsmokegames'
    scrape_webpage(url_to_scrape)

