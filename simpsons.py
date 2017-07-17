import requests
import string
import csv
import re

from bs4 import BeautifulSoup

WEBSITE = 'http://www.springfieldspringfield.co.uk/'

def get_words(text):
    regex = re.compile("(\w[\w']*\w|\w)")
    text = text.lower()
    return regex.findall(text)


def get_episodes_list():
    r = requests.get('http://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=the-simpsons')
    bs = BeautifulSoup(r.text, 'html.parser')
    return [i['href'] for i in bs.find_all('a', class_='season-episode-title')]

def get_script(episode_url):
    r = requests.get(episode_url)
    bs = BeautifulSoup(r.text, 'html.parser')
    s = bs.find('div', class_='episode_script')
    return s.text



word_count = dict()
episodes_urls = get_episodes_list()

for url in episodes_urls:
    ep = url[-6:]
    print('[%s] Getting script' % ep)
    script = get_script(WEBSITE + url)
    print('[%s] Script downloaded' % ep)

    words = get_words(script)
    ep_count = dict()

    for w in words:
        try:
            word_count[w] += 1
        except KeyError:
            word_count[w] = 1

        # this second block is here because sometimes that may be a word that is
        # not in the episode but it is in the total count. then, it needs to
        # check if the key exists in different blocks
        try:
            ep_count[w] += 1
        except KeyError:
            ep_count[w] = 1

    print('[%s] Writing csv' % ep)
    with open('./episodes/' + ep + '.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in ep_count.items():
            writer.writerow([key, value])
    print()

print('Writing total count to csv:')
with open('total_count.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in word_count.items():
        writer.writerow([key, value])

