from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import os

website = 'https://books.toscrape.com/'

option = webdriver.ChromeOptions()

# Initialize the WebDriver
driver = webdriver.Chrome(options=option)

def web_scraping():

    try:
        product_list = [["id", "product_description_link", "price", "product_image"]]

        page_number = 1

        url = driver.get(f"{website}catalogue/page-{page_number}.html")


        while True:
            
            list_of_data = driver.find_elements(By.XPATH, "//section/div/ol/li")
            
            if not list_of_data:
                break  # Exit the loop if no more data

            for id, product in enumerate(list_of_data, start=len(product_list)):
                product_image_div = product.find_element(By.TAG_NAME, "img")
                product_image = product_image_div.get_attribute("src") if product_image_div else "Not available"

                product_description_link_div = product.find_element(By.TAG_NAME, "h3")
                if product_description_link_div:
                    product_description_link = product_description_link_div.find_element(By.TAG_NAME, "a")
                    product_description_link = product_description_link.get_attribute("href") if product_description_link else "Not Available"
                else:
                    product_description_link = "Not Available"

                price_div = product.find_element(By.CLASS_NAME, "product_price")
                price = price_div.find_element(By.TAG_NAME, "p").text if price_div else "Not Available"

                product_list.append([id, product_description_link, price, product_image])
        
            # Save data to CSV
            if not os.path.exists('data'):
                os.makedirs('data')

            # Append data to CSV file
            with open('data/links.csv', 'a', newline='') as file:
                writer = csv.writer(file, delimiter='|')
                writer.writerows(product_list)
            
            print(f"Saved {len(product_list) - 1} links to CSV.")

            # Get next page 
            next_element = driver.find_element(By.CLASS_NAME, "next")
            if not next_element:
                break
            
            page_number += 1  # Move to the next page

    finally:
        input("Press Enter to quit the browser...")
        driver.quit()



def main():
    
    try:
        web_scraping()  # Call the function
    except:
        print("Error occurred while scraping data. Please try again later.")

        
if __name__ == "__main__":
    main()