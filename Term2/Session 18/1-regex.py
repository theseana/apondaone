import re
import requests
from myFUnction import download_image

url = "https://bama.ir/car/ssang-yong/actyon"
site_data = requests.get(url)

images_link = re.findall('<img src=\"(.+\.png)"', site_data.text) 
for link in images_link:
    download_image(link)