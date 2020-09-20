import requests

from requests.adapters import HTTPAdapter

session = requests.Session()

session.mount('http://', HTTPAdapter(max_retries=3))

session.mount('https://', HTTPAdapter(max_retries=3))

try:
    r = session.get('https://www.fakewebsite.com', timeout=5)
except requests.exceptions.RequestException as e:
    print(e)

