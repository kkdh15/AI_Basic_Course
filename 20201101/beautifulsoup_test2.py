import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/"
req = requests.get(url)
html = req.text

soup = BeautifulSoup(html,'html.parser')
select = soup.title.string
print(select)