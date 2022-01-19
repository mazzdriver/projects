import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://yandex.ru/news?msid=1639047702.76222.97685.514979&mlid=1639047105.glob_225&utm_medium=topnews_news&utm_source=morda_desktop"
r = requests.get(URL_TEMPLATE)

soup = bs(r.text, "html.parser")
article_title = soup.find_all('h2', class_='mg-card__title')
for name in article_title:
    print(name.a['h2'])
