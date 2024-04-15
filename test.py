
import requests
import waybackpy


import re

# def extract_full_timestamp(url):
#     # Use regular expression to find the timestamp in the Wayback Machine URL
#     match = re.search(r'/web/(\d{14})/', url)
#     if match:
#         return match.group(1)
#     else:
#         return "Timestamp not found in URL"


url = "https://www.lamborghini.com/en-en"
user_agent = "my new app's user agent"
# cdx_api = WaybackMachineCDXServerAPI(url, user_agent)


# Create a WaybackMachineAPI object for the URL
wayback = waybackpy.WaybackMachineAvailabilityAPI(url)
wayback.near()

# Get a list of archive snapshots
snapshots = wayback.snapshots()

a2 = []

# year segeration: 

for item in snapshots:
   if (item.statuscode < str(300)): 
           #print(item.archive_url)
           a2.append(item.archive_url)

print(a2)
       
   
   