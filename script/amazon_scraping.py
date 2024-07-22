import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.amazon.in/')

soup = BeautifulSoup(r.text, 'html.parser')

image_parent = soup.find("div", class_="a-row a-carousel-controls a-carousel-row a-carousel-has-buttons a-carousel-overlay-buttons a-carousel-rounded-buttons").find("div", class_="a-carousel-row-inner").find_all("div", class_="a-carousel-col")

image = image_parent[1].find("div", class_="a-carousel-viewport").find("ol", class_="a-carousel").find_all("li")

for i in image:
    image = i.find("div", class_="gw-ftGr-desktop-hero").find("img")
    print(image.get("src"))


