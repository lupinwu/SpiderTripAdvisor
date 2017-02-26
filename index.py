from bs4 import BeautifulSoup
import requests

url = 'https://github.com/mugglecoding/Plan-for-combating.git'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)
