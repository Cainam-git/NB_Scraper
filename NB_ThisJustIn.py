# Imports
import datetime
import requests
from bs4 import BeautifulSoup


def print_layout():
    """Print out a basic layout at the top of the screen."""
    # Basic layout for top of screen
    print("------------------------------\n"
          "|Recent News - Nieuwsblad.be:| "
          "\n------------------------------")
    # Add some time details from the 'get_current_time' function
    get_current_time()
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


def get_current_time():
    """Prints out the current time, time since last article went live and the difference."""
    # Retrieve current time
    current_date_time = datetime.datetime.now()

    # Convert 'scraped time' to a DateTime object 'last_update_time
    last_update_hour = get_time_list(article_time)[0].split(":")[0]
    last_update_minutes = get_time_list(article_time)[0].split(":")[1]
    last_update_time = datetime.datetime(current_date_time.year, current_date_time.month, current_date_time.day,
                                         int(last_update_hour), int(last_update_minutes))

    # Calculate difference based on current time and 'last_update_time'
    difference_time = current_date_time - last_update_time
    difference_time_seconds = difference_time.seconds

    # Use 'difference_time' and convert TimeDelta to a string
    difference_hours, remainder = divmod(difference_time_seconds, 3600)
    difference_minutes, difference_seconds = divmod(remainder, 60)
    difference_time_formatted = '{:02}:{:02}'.format(int(difference_hours), int(difference_minutes))

    # Print out current time, the (time of the) last update and the difference in minutes
    print("Current time:             " + current_date_time.strftime("%H:%M"))
    print("Last update:              " + last_update_time.strftime("%H:%M"))
    print("Time since last article:  " + difference_time_formatted)


if __name__ == '__main__':
    # Prepare source for scraping
    source = requests.get('https://nieuwsblad.be').text

    # Initialize soup instance
    soup = BeautifulSoup(source, 'lxml')

    # Find all 7 "This just in" articles and put them in 'contents'
    contents = soup.find_all('a', {'class': 'link-clean link-clean--delta'})

    # Find the time the article went 'live' and put it in 'time'
    article_time = soup.find_all('div', {'class': 'list-numbered__content'})

    # Print basic layout
    print_layout()

    # Iterate over all the articles and print out article, article number and link
    # Content[0] = index, Content[1] = article tags and attributes
    for content in enumerate(contents):
        print("#" + str(content[0] + 1) + " - " + get_time_list(article_time)[content[0]] + " - " +
              content[1].get_text().strip() + ".")
        print(content[1].get('href'))

        # Print a newline except if the last article has already been printed
        if content[0] != 6:
            print("\n")
