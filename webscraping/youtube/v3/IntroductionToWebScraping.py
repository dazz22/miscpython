# Tutorial Introduction To Web Scraping (with Python and Beautiful Soup) found @
# https://youtu.be/XQgXKtPSzUI

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.newegg.com/global/au/Video-Cards-Video-Devices/Category/ID-38"

# opening connection to page
uClient = uReq(my_url)
# loading html into variable
page_html = uClient.read()
# closing connection
uClient.close()

# parse page with Beutiful Soup
page_soup = soup(page_html, "html.parser")
# print the H1 tag
print(page_soup.h1)

containers = page_soup.findAll("div", {"class": "item-container"})
print(len(containers))

container = containers[0]
for container in containers:
    print(container.div.div.a.img["title"])
    print(container.findAll("a", {"class": "item-title"}))
    print(container.findAll("li", {"class": "price-current"}))
