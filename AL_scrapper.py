import requests
from bs4 import BeautifulSoup

page = requests.get("https://myanimelist.net/animelist/Eujh1n")

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

html = list(soup.children)[2]

body = list(html.children)[3]

l_cont = list(body.children)[5]

l_block = list(l_cont)[5]

l_all_anime = list(l_block)[1]

table = list(l_all_anime)[5]

print("yo")