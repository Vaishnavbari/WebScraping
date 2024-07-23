from bs4 import BeautifulSoup
import requests

# custom_headers = {
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
#     'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, br, zstd',
#     'Accept': '*/*',
#     'Referer': 'https://www.amazon.com/'

# }

custom_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

url = "https://www.amazon.com/b?node=12097479011"

response = requests.get(url=url, headers=custom_headers)

# print(response.text)

def amazon_scraping():
   
    try:
        soup = BeautifulSoup(response.text, "html.parser")

        # print(soup.prettify())

        # page_div = soup.find("div",  id="a-page")

        search_div = soup.find("div",  id="search")

        desktop_div = search_div.find("div", class_="s-opposite-dir") 


        matching_dir = desktop_div.find("div", class_="s-matching-dir")


        inner_col = matching_dir.find("div", class_="sg-col-inner")

        data_component_type = inner_col.find("span", attrs={"data-component-type": "s-search-results"})


        main_slot = data_component_type.find("div", attrs={"class": "s-main-slot"} )

        result_list = main_slot.find_all("div", attrs={"class": "s-result-item"})[1:]

        print(result_list)
        print("\n\n")

        for index, result in enumerate(result_list, start=2):

            # print(index , "start" + "="*100)


            # main_result_div = result.find("div", attrs={"class": "sg-col-inner"})

            product_div = result.find("div", attrs={"cel_widget_id": f"MAIN-SEARCH_RESULTS-{index}"})
            if bool(product_div):
                print(f"MAIN-SEARCH_RESULTS-{index}")

            section = product_div.find("span", class_="a-declarative").find("div", class_="a-section")

            puisg_row = section.find("div", class_="puisg-row")

            #  Get Image Data 
            product_image = puisg_row.find("div", class_="puis-list-col-left") #image parent 

            inner_col = product_image.find("div", class_="puisg-col-inner")

            image_component = inner_col.find("div", class_="s-product-image-container")

            inner_component = image_component.find("div", class_="aok-relative")

            image_data = inner_component.find("img") # image-data

            image_src = image_data.get("src") if image_data else None

            # Get Product Description 
            product_description = puisg_row.find("div", class_="puis-list-col-right") # image Description 
            
            product_description_inner_col = product_description.find("div", class_="puisg-col-inner")

            product_description_section = product_description_inner_col.find("div", class_="a-section") # product description section 

            title_component = product_description_section.find("div", attrs={"data-cy":"title-recipe"})

            product_name_component = title_component.find("h2")

            product_description_link = product_name_component.find("a").get("href")  # image description link 

            product_name = product_name_component.find("a").find("span").text  # product name 

            print(">>>>>>>>>>>>", product_name)

            # Get Product reviews
            product_reviews_section = product_description_section.find("div", attrs={"data-cy":"reviews-block"})

            product_review = product_reviews_section.find("i").span.text # product review 
              
            review_count = product_reviews_section.find("span", class_="s-underline-text").text # Total review count 

            # Get  Price 

            price_component = product_description_section.find("div", class_="puisg-row")

            price_recipe = price_component.find("div", attrs={"data-cy":"price-recipe"})
            # print(price_recipe,"\n")
            
            # print(price_recipe.find("span", attrs={"aria-hidden" : "true"}).find("span", class_="a-price-whole"))







      
             

            

            




    except Exception as e:
        # amazon_scraping()
        print(e)



if response.status_code == 200 :

    amazon_scraping()
else:
    amazon_scraping()
