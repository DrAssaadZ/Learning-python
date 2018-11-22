# image scrapper
from bs4 import BeautifulSoup as bs
import requests

search = input("Enter search term:")
params ={'q': search}
r = requests.get("https://www.bing.com/search", params=params)

soup = bs(r.text, "html.parser")
# print(soup.prettify())  #prints html code
result = soup.find("ol", {'id': 'b_results'})
links = result.findAll("li", {'class': 'b_algo'})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)

