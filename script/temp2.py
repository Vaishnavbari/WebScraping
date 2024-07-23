from bs4 import BeautifulSoup
import requests
import pandas as pd

custom_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

url = "https://www.amazon.com/b?node=12097479011"

response = requests.get(url=url, headers=custom_headers)
soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all("div", attrs={"cel_widget_id": lambda x: x and "MAIN-SEARCH_RESULTS-" in x})

product_data = []

for index, data in enumerate(results):

    try:
        title_component = data.find("div", attrs={"data-cy":"title-recipe"})
        product_name = title_component.find("span", class_="a-text-normal").text

        product_reviews_section = data.find("div", attrs={"data-cy":"reviews-block"})
        product_review = product_reviews_section.find("i").span.text if product_reviews_section.find("i") else "No review"
        review_count = product_reviews_section.find("span", class_="s-underline-text").text if product_reviews_section.find("span", class_="s-underline-text") else "No reviews"

        product_image = data.find("img")
        price_recipe = data.find("div", attrs={"data-cy":"price-recipe"})
        price = price_recipe.find("span", class_="a-offscreen") if price_recipe else None

        product_data.append({
            "id": index,
            "product_name": product_name,
            "product_review": product_review,
            "review_count": review_count,
            "product_image": product_image.get("src"),
            "price": price.text if price else "price not set"
        })

    except AttributeError as e:
        print(f"Error processing product {index}: {e}")

# Convert the collected data to a pandas DataFrame
df = pd.DataFrame(product_data)

# Write the DataFrame to an Excel file
df.to_csv('profiles1.xlsx', index=False)

print("Data has been written to profiles1.xlsx")
