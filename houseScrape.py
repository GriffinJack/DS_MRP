from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def HouseDetails(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = (soup.find('span', {'class':'title title--h1 price'}).text).strip()
    address = (soup.find('div', {'class':'title--h2 u-no-margins'}).text)
    results = soup.find_all('ul', {'class' : 'property-features-list'})
    labels = np.array(['Price','Adress'])
    values = np.array([price, address])

    for i in results:
        for j in i.find_all('span', {'class': 'value'}):
            if len(j.get_text().split('                \n')) == 1:
                values = np.append(values, j.get_text().strip())
            else:
                return None

    for i in results:
        for j in i.find_all('span', {'class': 'label'}):
            if len(j.get_text().split('                \n')) == 1:
                labels = np.append(labels, j.get_text().strip())
            else: 
                return None

    dict = {}

    for A, B in zip(labels,values):
        dict[A] = B

    return(dict)
