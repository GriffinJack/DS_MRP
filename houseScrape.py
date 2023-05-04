from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def HouseDetails(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('ul', {'class' : 'property-features-list'})
    labels = np.array([])
    values = np.array([])

    for i in results:
        for j in i.find_all('span', {'class': 'value'}):
            values = np.append(values, j.get_text())

    for i in results:
        for j in i.find_all('span', {'class': 'label'}):
            labels = np.append(labels, j.get_text())

    dict = {}

    for A, B in zip(labels,values):
        dict[A] = B

    return(dict)



URL = 'https://www.royallepage.ca/en/property/alberta/calgary/617-55-avenue-sw/19600830/mlsa2044095/'


print(HouseDetails(URL))