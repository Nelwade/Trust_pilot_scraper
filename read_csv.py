from types import NoneType
from scrape import open_parse_link, get_title, reviews
import pandas as pd
import numpy as np
import time

from scrape import open_parse_link

store_name =[]
review_list = []
r1, r2, r3, r4, r5 = [], [], [], [], []
error = ["null", "null", "null", "null", "null",]


df = pd.read_csv('trustpilot.csv')

for URL in df["URL"][:20]:
    print(URL)
    soup = open_parse_link(URL)
    try:
        store_name.append(get_title(soup))
        review_list.append(reviews(soup))
    except AttributeError:
        print("Error")
        review_list.append(None)

for store_review in review_list:
    # print()
    # print(store_review)
    if store_review == None or store_review == []:
        r1.append(None)
        r2.append(None)
        r3.append(None)
        r4.append(None)
        r5.append(None)
    else:
        r1.append(store_review[0])
        r2.append(store_review[1])
        r3.append(store_review[2])
        r4.append(store_review[3])
        r5.append(store_review[4])
# initializes a dictionary with the Keys as the column names and values as the entry into each column
dictionary = {
  'Store Name': store_name,
  'Review 1': r1,
  'Review 2': r2,
  'Review 3': r3,
  'Review 4': r4,
  'Review 5': r5,
  }

df_new=pd.DataFrame(dict([(k,pd.Series(v)) for k,v in dictionary.items()]))
print(df_new)

# writes the data into sample.data csv
df_new.to_csv(''+'sample_data'+'.csv',encoding='utf-8-sig')
