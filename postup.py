import requests
from bs4 import BeautifulSoup
from lxml import html


class Postup:

    def postuplenie(self):
        url = 'https://mininuniver.ru/entrant/kak-i-kogda-k-nam-postupit'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        items = soup.find_all('div', class_='col-sm-4 col-md-3 p15')
        mass = []
        for n, i in enumerate(items, start=1):
            itemsName = i.find('div', class_='name h4').text.strip()
            soob = f'{n}. {itemsName}'
            mass.append(soob)
        return (mass)

    def pravilaSchool(self):
        url ='https://mininuniver.ru/entrant/kak-i-kogda-k-nam-postupit'
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'lxml')
        items = soup.find('div',id='collapse-1').find_all('div', class_='panel panel-default')
        mass = []
        for n, i in enumerate(items, start=1):
            itemsName = i.find('div', class_='panel-heading').text.strip()
            soob = f'{itemsName}\n'
            mass.append(soob)
        return (mass)

    def pravilaSPO(self):
        url = 'https://mininuniver.ru/entrant/kak-i-kogda-k-nam-postupit'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        items = soup.find('div', id='collapse-2').find_all('div', class_='panel panel-default')
        mass = []
        for n, i in enumerate(items, start=1):
            itemsName = i.find('div', class_='panel-heading').text.strip()
            soob = f'{itemsName}\n'
            mass.append(soob)
        return (mass)

    def pravilaMag(self):
        url = 'https://mininuniver.ru/entrant/kak-i-kogda-k-nam-postupit'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        items = soup.find('div', id='collapse-3').find_all('div', class_='panel panel-default')
        mass = []
        for n, i in enumerate(items, start=1):
            itemsName = i.find('div', class_='panel-heading').text.strip()
            soob = f'{itemsName}\n'
            mass.append(soob)
        return (mass)


