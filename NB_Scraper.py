# Imports
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    # Prepare source for scraping
    source = requests.get('https://nieuwsblad.be').text
    soup = BeautifulSoup(source, 'lxml')

    # Create variables
    summary = None
    link = None

    # Retrieve every article and link
    for article in soup.find_all('a', class_='link-complex'):
        # Check if text and link are available
        try:
            summary = article.header.h1.text
            link = article.get('href')

        # Handle any 'not-found' errors
        except Exception as e:
            print('Error: ' + str(e))

        # Print out results
        print(summary.strip())
        print(link)
