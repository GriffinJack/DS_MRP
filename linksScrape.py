from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np



def get_links(URL):
    

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    links = np.array([])
    web = 'https://www.royallepage.ca/en/property/alberta/calgary'

    for a in soup.find_all('a', href=True):
        if web in a['href']:
            links = np.append(links, a['href'])

    links = np.unique(links)

    return links


URL = 'https://www.royallepage.ca/en/search/homes/ab/calgary/1/?property_type=&house_type=&features=&listing_type=&lat=51.04511300000007&lng=-114.05714099999994&bypass=&address=Calgary&address_type=city&city_name=Calgary&prov_code=AB&display_type=gallery-view&da_id=&travel_time=false&school_id=&search_str=Calgary%2C+AB%2C+CAN&id_search_str=Calgary%2C+AB%2C+CAN&school_search_str=&travel_time_min=30&travel_time_mode=drive&travel_time_congestion=&min_price=0&max_price=5000000%2B&min_leaseprice=0&max_leaseprice=5000%2B&beds=0&baths=0&transactionType=SALE&keyword='


print(get_links(URL))