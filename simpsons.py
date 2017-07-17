import requests
import string
from bs4 import BeautifulSoup

WEBSITE = 'http://www.springfieldspringfield.co.uk/'

def remove_punctuation(text):
    table = dict((i, '') for i in string.punctuation)
    table = ''.maketrans(table)

    return text.translate(table)

def get_episodes_list():
    r = requests.get('http://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=the-simpsons')
    bs = BeautifulSoup(r.text, 'html.parser')
    return [i['href'] for i in bs.find_all('a', class_='season-episode-title')]

def get_script(episode_url):
    req = requests.get(episode_url)
    bs = BeautifulSoup(r.text, 'html.parser')
    s = bs.find('div', class_='episode_script')
    return s.text



episodes = get_episodes_list()
print(episodes)




