#web scrape anichart/MAL for anime
#https://myanimelist.net/anime/season
#https://anichart.net/Spring-2019

'''
class Anime:
    #this contains the attributes for a single anime show
    title = ""
    episodes = 0
    current_ep = 0
'''
import requests
from bs4 import BeautifulSoup
url = 'https://myanimelist.net/anime/season'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
titles = soup.find(class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-1 clearfix').find_all(class_='link-title')
print(titles)
#use soup to get all tags with titletext maybe?
#then put them in hashmap
#what do i want to do with the titles
#what other data do i want to store
#create an anime object maybe?


#<a href="https://myanimelist.net/anime/34134/One_Punch_Man_2nd_Season" class="link-title">One Punch Man 2nd Season</a>
#class= "seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-1 clearfix"
