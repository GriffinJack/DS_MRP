from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np



def get_links(URL, pageCount, URL2):
    links = np.array([])
    for i in range(pageCount):
        tempURL = URL + str(i+1) + URL2
        page = requests.get(tempURL)

        soup = BeautifulSoup(page.content, 'html.parser')

        web = 'https://www.royallepage.ca/en/property'

        for a in soup.find_all('a', href=True):
            if web in a['href']:
                links = np.append(links, a['href'])

    return np.unique(links)