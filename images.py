# image scraper, and download files
from bs4 import BeautifulSoup as bs
from PIL import Image
from io import BytesIO
import requests

search = input("Enter search term:")
params ={'q': search}
r = requests.get("https://www.bing.com/images/search", params=params)

soup = bs(r.text, "html.parser")
links = soup.findAll("a", {'class': 'thumb'})

for item in links:
    img_url = requests.get(item.attrs["href"])
    title = item.attrs["href"].split('/')[-1]
    img = Image.open(BytesIO(img_url.content))
    img.save("./scr_imgs/" + title, img.format)
