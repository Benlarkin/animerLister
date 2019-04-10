#web scrape anichart/MAL for anime
#https://myanimelist.net/anime/season
#https://anichart.net/Spring-2019
from animeClass import Anime
import requests
from bs4 import BeautifulSoup
url = 'https://myanimelist.net/anime/season'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

def title_scraping():
    titlesoup = soup.find(class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-1 clearfix').find_all(class_='link-title')
    seasonal_titles = []
    for title in titlesoup:
        seasonal_titles.append(title.text)
    #print(seasonal_titles)
    return seasonal_titles

def episode_scraping():
    episodesoup = soup.find(class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-1 clearfix').find_all(class_='eps')
    #getting error about find vs find all, want the spans that contains episode #, although it seems pointless right now
    #spans = episodesoup.find_all('span')
    print(episodesoup)
    episode_count = []
    for episode in episodesoup:
        episode_count.append(episode.text)
    #print(episode_count)
    return episode_count
episode_scraping()
'''
#imported animeClass above and create an instance of Anime object with the values for one punch man
#testing the Anime object
OPM = Anime("One Punch Man", 12, "Action", 15)
print(OPM.get_Genre())
'''

#use soup to get all tags with titletext maybe?
#then put them in hashmap
#what do i want to do with the titles
#what other data do i want to store
#create an anime object maybe?


#<a href="https://myanimelist.net/anime/34134/One_Punch_Man_2nd_Season" class="link-title">One Punch Man 2nd Season</a>
#class= "seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-1 clearfix"


#endgame is graphing/visualization
