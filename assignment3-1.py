import pandas as pd
import requests
import time
import json

#set parameters
host = "http://code001.ecsbdp.com"
country_data_list = []

#import the airports data to get the unique iso_country codes
airports = pd.read_csv('airports.csv', keep_default_na=False)
iso_codes = airports["iso_country"].dropna().unique()
print(f"number of unique countries found: {len(iso_codes)}")

#loop through the unique iso_country codes and make API calls to get the country data, then save it to a list. if there is no data then print the error code. also add a small delay between requests to avoid overwhelming the server.
for code in iso_codes:
    url = f"{host}/countries/{code}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        country_data_list.append(response.json())
    else:
        print(f"Failed for {code}: {response.status_code}")
    
    time.sleep(0.2)

#save the country data list to a json file
with open("country_data.json", "w") as f:
    json.dump(country_data_list, f, indent=4)
print("Saved country_data.json")