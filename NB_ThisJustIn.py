# Imports
from bs4 import BeautifulSoup
import requests


def print_layout():
    """Print out a basic layout at the top of the screen."""
    # Basic layout for top of screen
    print("--------------\n|Recent News:| \n--------------")
    print("\n")


def get_time_list(time_from_bs_obj):
    """Takes all scraped time attributes and stores them in a list."""
    # Iterate over 'time_from_bs_obj' and store every time in 'times_list'
    # Also check the type is not None
    times_list = []
    for times in enumerate(time_from_bs_obj):
        if times[1].get('data-number') is not None:
            times_list.append(times[1].get('data-number'))
    return times_list


if __name__ == '__main__':
    # Prepare source for scraping
    source = requests.get('https://nieuwsblad.be').text

    # Initialize soup instance
    soup = BeautifulSoup(source, 'lxml')

    # Find all 7 "This just in" articles and put them in 'contents'
    contents = soup.find_all('a', {'class': 'link-clean link-clean--delta'})

    # Find the time the article went 'live' and put it in 'time'
    time = soup.find_all('div', {'class': 'list-numbered__content'})

    # Print basic layout
    print_layout()

    # Iterate over all the articles and print out article, article number and link
    # Content[0] = index, Content[1] = article tags and attributes
    for content in enumerate(contents):
        print(get_time_list(time)[content[0]] + " #" + str(content[0] + 1) + " " + content[1].get_text().strip() + ".")
        print(content[1].get('href'))
        # Print a newline except if the last article has already been printed
        if content[0] != 6:
            print("\n")
