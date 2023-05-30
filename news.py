import requests
from bs4 import BeautifulSoup
from lxml import html

class News:
  def сalendar_events(self):
    url = 'https://mininuniver.ru/events?filter;dlya-kogo:abiturientu'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    items = soup.find_all('div', class_='event col-sm-6 col-xlg-4 p15')
    mass = []
    for n, i in enumerate(items, start=1):
      itemsName = i.find('a', i.get("href")).text.strip()
      itemsDate = i.find('div', class_='date').text
      items_url = i.find('a',href=True)
      items_urlGet = items_url.get('href')
      soob = f'{itemsDate}\n ' \
             f'{itemsName}\n ' \
             f'https://mininuniver.ru{items_urlGet}' \
             f'\n'
      mass.append(soob)
    return (mass[:5])

  def last_news(self):
    url = 'https://mininuniver.ru/about/news'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    items = soup.find_all('div', class_='grid-item col-sm-6 col-xlg-4 p15 wow fadeInUp')
    mass = []
    for n, i in enumerate(items,start=1):
      itemsName = i.find('a', i.get("href")).text.strip()
      items_url = i.find('a', href=True)
      items_urlGet = items_url.get('href')
      soob = f' {itemsName}\n ' \
             f'https://mininuniver.ru{items_urlGet}' \
             f'\n'
      mass.append(soob)
    return (mass[:5])







