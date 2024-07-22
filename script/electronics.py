from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.amazon.in/s?k=electronic&crid=232L7QDDOV1L2&sprefix=electronic%2Caps%2C194&ref=nb_sb_noss_1")

if response.status_code == 200 :

    soup = BeautifulSoup(response.text, "html.parser")

    rush_component = soup.find("div",  id="search").find("div", class_="s-desktop-width-max s-desktop-content s-opposite-dir s-wide-grid-style sg-row")

    main_div = rush_component.find("div", class_="sg-col-inner")

    main_slot = main_div.find("span", class_="rush-component s-latency-cf-section").find("div", class_="s-main-slot s-result-list s-search-results sg-row")

    section = main_slot.find_all("div", class_="a-section a-spacing-none")

else:
    print("Error",response.status_code)



