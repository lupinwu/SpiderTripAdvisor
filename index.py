from bs4 import BeautifulSoup
import requests

url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-c47-New_York_City_New_York.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
titles = soup.select('div.property_title > a')
imgs = soup.select('img[width="160"]')
print(titles, imgs)

