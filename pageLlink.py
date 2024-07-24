from bs4 import BeautifulSoup
import requests
import csv
import os

base_url = "https://www.amazon.com/"

custom_headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
    }

def inner_url_scraping(inner_url):

    url =f"{base_url}inner_url"
    page =  requests.get(url=url, headers=custom_headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())


def web_scraping():
   

    user_keyword = input("Enter your keyword: ").strip()

    page_number = 1

    product_list = [["id", "product_name", "product_review", "review_count", "product_image", "price"]]

    while True:
        url = f"{base_url}s?k={user_keyword}&page={page_number}&crid=9C9WDWWLV3GT&sprefix=mackbook%2Caps%2C276&ref=nb_sb_noss_2"

        print("Scraping URL:", url)

        response = requests.get(url=url, headers=custom_headers)
        if response.status_code != 200:
            print("Failed to retrieve the webpage.")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        results = soup.find_all("div", attrs={"cel_widget_id": lambda x: x and "MAIN-SEARCH_RESULTS-" in x})

        for index, data in enumerate(results, start=len(product_list)):
            if not data:
                continue

            product_name = data.find("span", class_="a-text-normal")
            

            product_name = product_name.text if product_name else "Not available"

            product_description_link = data.find("a", class_="a-link-normal")
            if product_description_link:
                inner_url =product_description_link.get("href")
                inner_url_scraping(inner_url)

            product_reviews_section = data.find("div", attrs={"data-cy":"reviews-block"})
            if product_reviews_section:
                product_review = product_reviews_section.find("i")
                product_review = product_review.span.text if product_review else "Not available"
                
                review_count = product_reviews_section.find("span", class_="s-underline-text")
                review_count = review_count.text if review_count else "Not available"
            else:
                product_review = "Not available"
                review_count = "Not available"

            product_image = data.find("img")
            product_image = product_image.get("src") if product_image else "Not available"

            price_recipe = data.find("div", attrs={"data-cy":"price-recipe"})
            if price_recipe:
                price = price_recipe.find("span", class_="a-offscreen")
                price = price.text if price else "Not Available"
            else:
                price = "Not Available"

            product_list.append([index, product_name, product_review, review_count, product_image, price])

        # Save data to CSV
        if not os.path.exists('csv'):
            os.makedirs('csv')

        with open(f'csv/{user_keyword}.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerows(product_list)

        print(f"Data for keyword '{user_keyword}' has been saved to csv/{user_keyword}.csv")

        # Check for next page
        next_page_element = soup.find('a', class_="s-pagination-next")
        if not next_page_element or 's-pagination-disabled' in next_page_element.get('class', []):
            break

        page_number += 1
        print(f"Scraped Page {page_number}")

web_scraping()  # Call the function
