# Imports
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    # Prepare source for scraping
    source = requests.get('https://nieuwsblad.be').text

    # Initialize soup instance
    soup = BeautifulSoup(source, 'lxml')

    # Basic layout for top of screen
    print("|----------|\n|NET BINNEN|\n|----------|")
    print("\n")

    # Find all 7 "This just in" articles and put them in contents
    contents = soup.find_all('a', {'class': 'link-clean link-clean--delta'})
    # Find the time the article went 'live'
    time = soup.find_all('div', {'class': 'list-numbered__content'})

    # Iterate over all the articles and print out article, article number and link
    # Content[0] = index, Content[1] = article tags and attributes
    for content in enumerate(contents):
        print("#" + str(content[0] + 1) + " " + content[1].get_text().strip() + ".")
        print(content[1].get('href'))
        print("\n")

    # To Do: figure out how to correctly print out time article went 'live'
    # for times in enumerate(time):
    # if times[1] is not None:
    # print(times[1].get('data-number'))
