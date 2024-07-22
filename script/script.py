from bs4 import BeautifulSoup

file = """

<!doctype html>
<html>
  <head>
    <title>This is the title of the webpage!</title>
  </head>
  <body>
    <p class="heheheh" >This is an example paragraph. Anything in the <strong>body</strong> tag will appear on the page, just like this <strong>p</strong> tag and its contents.</p>
  </body>
</html>

"""


soup = BeautifulSoup(file, 'html.parser')

# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
print(soup.title.parent.name)
# print(soup.p)
# print(type(soup.p['class']))
# print(soup.p.attrs)
# print(soup.p.string)
# print(soup.a)
# print(soup.find_all('p'))
# print(soup.find_all('a'))
# print(soup.find_all('a')[0])
# print(soup.find_all('a')[0].string)
# print(soup.find_all('a')[0]['href'])
# print(soup.find_all('a')[0].parent.name)
# print(soup.find_all('a')[0].parent.parent.name)
# print(soup.find_all('a')[0].parent.parent.parent.name)
# print(soup.find_all('a')[0].parent.parent.parent.parent.name)
# print(soup.find_all('a')[0].parent.parent.parent.parent.parent.name)
# print(soup.find_all('a')[0].parent.parent.parent.parent.parent.parent.name)




    