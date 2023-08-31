from houseScrape import HouseDetails
from linksScrape import get_links
import numpy as np
import pandas as pd

URL1 = 'https://www.royallepage.ca/en/search/homes/ab/calgary/'

pageCount = 20

URL2 = '?search_str=Calgary%2C+AB%2C+CAN&csrfmiddlewaretoken=p6AM4vstnPaQr9s7DLNi9xp3jX19dQm1cZsIbkdlVWQNnizxcksadKJIr8qSTT9T&property_type=7%2C8&house_type=&features=&listing_type=&lat=51.04511300000007&lng=-114.05714099999994&upper_lat=&upper_lng=&lower_lat=&lower_lng=&bypass=&radius=&zoom=&display_type=gallery-view&travel_time=false&travel_time_min=30&travel_time_mode=drive&travel_time_congestion=&da_id=&segment_id=&tier2=False&tier2_proximity=0&address=Calgary&method=homes&address_type=city&city_name=Calgary&prov_code=AB&school_id=&min_price=0&max_price=5000000%2B&min_leaseprice=0&max_leaseprice=5000%2B&beds=0&baths=0&transactionType=SALE&sfproperty_type%5B7%5D=7&sfproperty_type%5B8%5D=8&keyword=&sortby='

links = get_links(URL1, pageCount, URL2)


data = np.array([])

for link in links:
    temp = HouseDetails(link)
    if temp == None:
        continue
    data = np.append(data, temp)

df = pd.DataFrame.from_records(data)

df.to_csv("houseData.csv")
