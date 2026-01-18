from playwright.sync_api import sync_playwright
from datetime import datetime
from bs4 import BeautifulSoup
import requests

currentYear = datetime.now().year
link = input('Enter a URL: ').strip().replace("https://","").replace("http://","").split("/")[0]
api = f"https://rdap.verisign.com/com/v1/domain/{link}"
data = requests.get(api).json()

print(' ')
print('Domain: ' + data['ldhName'])
# strptime = string parse time --> Parse time, then format time (strftime) = String Format Time
registered_dt = datetime.strptime(data['events'][0]['eventDate'], "%Y-%m-%dT%H:%M:%SZ")
expiration_dt = datetime.strptime(data['events'][1]['eventDate'], "%Y-%m-%dT%H:%M:%SZ")
lastChanged_dt = datetime.strptime(data['events'][2]['eventDate'], "%Y-%m-%dT%H:%M:%SZ")

if registered_dt.year >= currentYear - 2:
    print('( Made recently )')
else:
    print('[ Old domain ]')

print(' ')
print('Registered: ' + registered_dt.strftime("%b %d, %Y"))
print('Expiration: ' + expiration_dt.strftime("%b %d, %Y"))
print(' ')
print('Last Changed: ' + lastChanged_dt.strftime("%b %d, %Y"))
if lastChanged_dt.year >= currentYear - 2:
    print("( Changed Recently )")
else:
    print("[ NOT Changed Recently ]")
print(' ')
print(currentYear)
print(' ')
