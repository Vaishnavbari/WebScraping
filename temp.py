from bs4 import BeautifulSoup
import requests
import csv 
import pandas as pd

custom_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

url = "https://www.amazon.com/s?k=mackbook+pro+13%22+case&crid=2CTK2HW58J9BJ&sprefix=mack%2Caps%2C266&ref=nb_sb_ss_pltr-sample-20_8_4"

response = requests.get(url=url, headers=custom_headers)

soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all("div", attrs={"cel_widget_id": lambda x: x and "MAIN-SEARCH_RESULTS-" in x})

product_list = [["id", "product_name", "product_review", "review_count", "product_image", "price"]]

for index, data in enumerate(results, start=1):

    title_component = data.find("div", attrs={"data-cy":"title-recipe"})
    product_name = title_component.find("span", class_="a-text-normal").text

    product_reviews_section = data.find("div", attrs={"data-cy":"reviews-block"})
   
    product_review = product_reviews_section.find("i").span.text

    review_count = product_reviews_section.find("span", class_="s-underline-text").text # Total review count 

    product_image = data.find("img")

    price_recipe = data.find("div", attrs={"data-cy":"price-recipe"})
    
    try:

         price = price_recipe.find("span", class_="a-offscreen").text 
    except :
        price = "Not Available"

   
    product_list.append([ index, product_name,product_review, review_count, product_image.get("src"), price if price else "price not set"])


# print(product_list)
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(product_list)
        

    
