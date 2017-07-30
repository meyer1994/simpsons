import requests
import string
import csv
import re

from collections import Counter

from bs4 import BeautifulSoup

# base website url
WEBSITE = 'http://www.springfieldspringfield.co.uk/'

def get_words(text):
    '''
    Get words.

    Function created to get all the words from a string. It uses regex from
    this StackOverflow question:
        https://stackoverflow.com/questions/12705293/regex-to-split-words-in-python/12705513

    Args:
        text: An string to get the words from.

    Returns:
        A list with all the words from the string.
    '''

    regex = re.compile("(\w[\w']*\w|\w)")
    text = text.lower()
    return regex.findall(text)


def get_episodes_list():
    '''
    Get episodes list.

    A simple function that will return all the episodes' script urls from the
    website.

    Returns:
        List with urls for the scripts.
    '''

    r = requests.get(WEBSITE + 'episode_scripts.php?tv-show=the-simpsons')
    bs = BeautifulSoup(r.text, 'html.parser')
    return [ i['href'] for i in bs.find_all('a', class_='season-episode-title') ]


def get_script(episode_url):
    '''
    Get script.

    Gets the scripts, as strings, from the website.

    Args:
        episode_url: Url of where to get the script from.

    Returns:
        String, unedited, containing the script.
    '''

    r = requests.get(episode_url)
    bs = BeautifulSoup(r.text, 'html.parser')
    s = bs.find('div', class_='episode_script')
    return s.text



total_count = Counter()
episodes_urls = get_episodes_list()

for url in episodes_urls:
    ep = url[-6:]
    print('[%s] Getting script' % ep,)
    script = get_script(WEBSITE + url)
    print('Script downloaded')

    words = get_words(script)
    ep_count = Counter(words)

    # add to total
    total_count.update(ep_count)

    print('Writing csv')
    with open('./episodes/' + ep + '.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in ep_count.items():
            writer.writerow([key, value])
    print('-----------------')

print('\nWriting total count to csv:')
with open('total_count.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in total_count.items():
        writer.writerow([key, value])

print('FIN!')
