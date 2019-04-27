from pprint import pprint
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

API_KEY = os.environ.get("ZILLOW_API_KEY", "OOPS")

state = "ct"
city = "new%20haven" # todo: use some package or module (requests?) to convert this from human-friendly input "New Haven"
url = f"https://www.zillow.com/webservice/GetRegionChildren.htm?zws-id={API_KEY}&state={state}&city={city}&childtype=neighborhood"
print("URL", url)

response = requests.get(url)
print("RESPONSE", response.status_code, type(response))
#print(response.text)

soup = BeautifulSoup(response.text, features="lxml") # pass "features" to suppress warning message

#breakpoint()

#region = soup.find("response").find("region")
subregion_type = soup.find("response").find("subregiontype")

hoods_count = soup.find("response").find("list").find("count")
hoods = soup.find("response").find("list").find_all("region")

print(f"FOUND {hoods_count.text} {subregion_type.text.upper()}(S):")

for hood in hoods:
    h = {
        "id": hood.find("id").text,
        "name": hood.find("name").text,
        #"zindex": hood.find("zindex").text, # <zindex currency="USD">126400</zindex>
        "url": hood.find("url").text,
        "lat": hood.find("latitude").text,
        "long": hood.find("longitude").text,
    }
    pprint(h)
