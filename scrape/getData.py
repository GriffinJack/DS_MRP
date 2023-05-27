from houseScrape import HouseDetails
from linksScrape import get_links
import numpy as np

URL1 = 'https://www.royallepage.ca/en/search/homes/ab/calgary/'

pageCount = 2

URL2 = '/?property_type=&house_type=&features=&listing_type=&lat=51.04511300000007&lng=-114.05714099999994&bypass=&address=Calgary&address_type=city&city_name=Calgary&prov_code=AB&display_type=gallery-view&da_id=&travel_time=false&school_id=&search_str=Calgary%2C+AB%2C+CAN&id_search_str=Calgary%2C+AB%2C+CAN&school_search_str=&travel_time_min=30&travel_time_mode=drive&travel_time_congestion=&min_price=0&max_price=5000000%2B&min_leaseprice=0&max_leaseprice=5000%2B&beds=0&baths=0&transactionType=SALE&keyword='

links = get_links(URL1, pageCount, URL2)

data = np.array([])

count = 1
for link in links:
    temp = HouseDetails(link)
    if temp == None:
        continue
    print(temp)
    print(link)
    print(count, "-------------------------------------------------------------------")
    count+= 1
    data = np.append(data, temp)

