from houseScrape import HouseDetails
import numpy as np 
import pandas as pd 

URL = 'https://www.royallepage.ca/en/property/alberta/calgary/158-hampstead-circle-nw/19616079/mlsa2044595/'
URL2 = 'https://www.royallepage.ca/en/property/alberta/calgary/17-west-cedar-point-sw/19618635/mlsa2045368/'

house1 = HouseDetails(URL)
house2 = HouseDetails(URL2)

df = pd.DataFrame.from_records([house1,house2])

print(df)
