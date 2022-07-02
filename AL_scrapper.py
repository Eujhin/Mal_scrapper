import requests
from bs4 import BeautifulSoup

page = requests.get("https://myanimelist.net/animelist/Eujh1n")

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

list(soup.children)