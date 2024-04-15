
import requests
from waybackpy import WaybackMachineCDXServerAPI
from waybackpy import WaybackMachineAvailabilityAPI
import pandas as pd
from tqdm import tqdm
import os


import re

# Function to extract the full timestamp from a Wayback Machine URL
def extract_full_timestamp(url):
    # Use regular expression to find the timestamp in the Wayback Machine URL
    match = re.search(r'/web/(\d{14})/', url)
    if match:
        return match.group(1)
    else:
        return "Timestamp not found in URL"
    



# Specify the filename
filename = 'url.txt'



    

start_year = 2017
end_year = 2023

start_month = 3
max_month = 12

DEFAULT_HOUR = 12
DEFAULT_MINUTE = 30
DEFAULT_DAY = 15

HTTP_OPTION = True



#Usage: 

# url = "google.com"
# user_agent = "my new app's user agent"
# cdx_api = WaybackMachineCDXServerAPI(url, user_agent)
# Create a WaybackMachineAPI object for the URL
# wayback = WaybackMachineCDXServerAPI(url)

# # Get a list of archive snapshots
# snapshots = wayback.snapshots()

list = pd.read_csv('./url_generation/testWebsitesURL.csv')

snapshots_table = pd.DataFrame(columns=["snapshots_url"])
#url_table = pd.DataFrame()
# availability_api = WaybackMachineAvailabilityAPI(url)

# snapshots_table is a pandas dataframe, usused for now

def extract_sample_snapshot(list):
    with open(filename, 'a') as file:
        for u in list['Domain']:
            availability_api = WaybackMachineAvailabilityAPI(u)
            curr_year = start_year
            for curr_year in tqdm(range(start_year, end_year + 1), desc='Years progress', leave=False):
                curr_month = start_month
                while curr_month <= max_month:
                    availability_api.near(year=curr_year, month=curr_month, day=DEFAULT_DAY, hour=DEFAULT_HOUR, minute=DEFAULT_MINUTE)
                    if (availability_api.json["archived_snapshots"]=={}):
                        curr_month += 3
                        print("No snapshot")
                        continue
                    # if (extract_full_timestamp(availability_api.json["archived_snapshots"]["closest"]["url"]) < "20170301000000"):
                    #     print("Old snapshot")
                    #     break
                    if (availability_api.json["archived_snapshots"]["closest"]["status"] < str(300)):
                        # pd
                    #snapshots_table = pd.concat([snapshots_table, pd.DataFrame([{"snapshots_url": url_json_obj.json["archived_snapshots"]["closest"]["url"]}])], ignore_index=True)
                        file.write(availability_api.json["archived_snapshots"]["closest"]["url"][7:] + "\n")
                        
                    curr_month += 3
                curr_year += 1

                # add a 2024.03:
            availability_api.near(year=2024, month=3, day=DEFAULT_DAY, hour=DEFAULT_HOUR, minute=DEFAULT_MINUTE)
            if (availability_api.json["archived_snapshots"]["closest"]["status"] < str(300)):
                # pd
                #snapshots_table = pd.concat([snapshots_table, pd.DataFrame([{"snapshots_url": url_json_obj.json["archived_snapshots"]["closest"]["url"]}])], ignore_index=True)
                # Write something to the file
                file.write(availability_api.json["archived_snapshots"]["closest"]["url"][7:] + "\n")




extract_sample_snapshot(list)

# print(snapshots_table)

       
   
   