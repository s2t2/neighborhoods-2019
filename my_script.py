import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ.get("ZILLOW_API_KEY", "OOPS")

state = "ct"
city = "new%20haven" # todo: use some package or module (requests?) to convert this from human-friendly input "New Haven"

url = f"https://www.zillow.com/webservice/GetRegionChildren.htm?zws-id={API_KEY}&state={state}&city={city}&childtype=neighborhood"

print("URL", url)

response = requests.get(url)

print("RESPONSE", response.status_code, type(response))

print(response.text)
