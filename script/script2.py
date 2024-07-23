import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')


# print content of request
soup = BeautifulSoup(r.text, 'html.parser')
article_title = soup.find("div", class_ ="text")
table_of_content = article_title.find("div", id="table_of_content")
list_of_table_of_content = table_of_content.find("ul").find_all("li")
for i in list_of_table_of_content:
    print(i.text)
    

