import bs4
import requests
from bs4 import BeautifulSoup as soup 
import sqlite3
from urllib2 import urlopen

my_url = 'https://www.traxsource.com/genre/20/techno/top'

# get the html
html = urlopen(my_url)

# html parsing
page_soup = soup(html, "html.parser")

containers = page_soup.findAll("a", { "class" : "com-artists" })


for container in containers:

    artist_Name = str(container.text)
	
    print(artist_Name)

#contain = containers[0]
#container = containers[0]

# run this script then type container.text
# list = str(container.text)
# print(list)