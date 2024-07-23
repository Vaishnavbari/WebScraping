from bs4 import BeautifulSoup
import requests

custom_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.amazon.in/s?k=electronic&crid=232L7QDDOV1L2&sprefix=electronic%2Caps%2C194&ref=nb_sb_noss_1'

}

url = "https://www.amazon.in/s?k=electronic&crid=232L7QDDOV1L2&sprefix=electronic%2Caps%2C194&ref=nb_sb_noss_1"

response = requests.get(url, custom_headers)


def amazon_scraping():
   
    try:
        soup = BeautifulSoup(response.text, "html.parser")


        # search_div = soup.find_all("div",  id="search")

        # print(">>>>>>>>>>>>>",search_div)

        # desktop_div = search_div.find("div", class_="s-desktop-width-max") 

        # matching_dir = desktop_div.find("div", class_="s-matching-dir")

        # inner_col = matching_dir.find("div", class_="sg-col-inner")

        # data_component_type = inner_col.find("span", attrs={"data-component-type": "s-search-results"})

        # print(">>>>>>>>>>>>>>>>>>>", matching_dir)

    except Exception as e:
        # amazon_scraping()
        print(e)



if response.status_code == 200 :
    amazon_scraping()
else:
    amazon_scraping()



