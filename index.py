from bs4 import BeautifulSoup
import requests
import time

url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-c47-New_York_City_New_York.html'
urls = ['http://www.tripadvisor.cn/Attractions-g60763-Activities-c47-oa{}-New_York_City_New_York.html'
        '#ATTRACTION_LIST'.format(str(i)) for i in range(30, 400, 30)]
urls.insert(0, url)


def get_attractions(url, data=None):
    response = requests.get(url)
    time.sleep(2)  # 每隔2秒请求一次,防止反爬虫
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.select('div.property_title > a[target="_blank"]')
    cates = soup.select('div.p13n_reasoning_v2')
    for title, cate in zip(titles, cates):
        data = {
            'title': title.get_text(),
            'cate': list(cate.stripped_strings),
        }
        print(data)


for single_url in urls:
    get_attractions(single_url)
