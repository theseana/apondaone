from bs4 import BeautifulSoup

import requests


url = "http://mydiba.me/"
site_data = requests.get(url)

soup = BeautifulSoup(site_data.content, 'html.parser')

a_tags = []
articles = soup.find_all("article")
for article in articles:
    a_tags.append(article.find_all("a", rel="bookmark"))
for a in a_tags:
    if a:
        print(a[0]["href"])
