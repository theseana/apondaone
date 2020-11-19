import requests


def download_image(link):
    response = requests.get(link)
    file = open(f"/cars/{link}.png", "wb")
    file.write(response.content)
    file.close()