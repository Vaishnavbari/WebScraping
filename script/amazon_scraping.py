import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.amazon.in/')

soup = BeautifulSoup(r.text, 'html.parser')

card_body = soup.find("div", id="pageContent")

card = card_body.find_all("div", id="gw-layout")

cards = card[0].find_all("div", class_="gw-card-layout")


for index, item in enumerate(cards, start=1):
    first_div = card_body.find("div", id=f"desktop-grid-{index}")
    title = first_div.find("div", class_="a-cardui-header").find("h2").text
    link = first_div.find("div", class_="a-cardui-footer").find("a")
    image_parent = first_div.find("div", class_="_fluid-quad-image-label-v2_style_fluidQuadImageLabelBody__3tld0")
    print(image_parent)




