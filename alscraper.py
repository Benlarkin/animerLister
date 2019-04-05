import urllib.request
from bs4 import BeautifulSoup

anime_page = ['https://myanimelist.net/anime/season']

page = urllib.request.urlopen(anime_page)

soup = BeautifulSoup(page, 'html.parser')

print(soup.get_text())
