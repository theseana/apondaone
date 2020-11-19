from bs4 import BeautifulSoup

import requests


url = "http://mydiba.me/"
site_data = requests.get(url)

soup = BeautifulSoup(site_data.content, 'html.parser')

imgs = soup.find_all("img", class_="attachment-indexm size-indexm wp-post-image")
for img in imgs:
    print(img['src'])
print(imgs)