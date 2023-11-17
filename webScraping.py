from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import csv

# declaring the function "getTitle()", which returns the title of the page from the attribute "h1"
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

print('')

# Open a connection to the specified URL and returns a response object.
html = urlopen('https://habr.com/ru/search/?q=%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F&target_type=posts&order=relevance')

# Creating a BeautifulSoup object
bs = BeautifulSoup(html, "html.parser")

#print (bs)

# getting the title of the page by calling function getTitle()
title = getTitle("https://habr.com/ru/search/?q=%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F&target_type=posts&order=relevance")
if title == None:
    print("Title could not be found")
    print('')
else:
    print("The title is: ", title)
    print('')

# getting the names of articles we are searching about and storing them in a string array called "nameList"
nameList = bs.findAll('h2', {'class': 'tm-title'})

# getting the authors names of these articles and storing them in a string array called "authorsList"
authorsList = bs.find_all('a', class_='tm-user-info__username')

# getting the links of these articles and storing them in a string array called "linkList"
linkList = bs.find_all('a', class_='tm-title__link')

# deffining the iterator "i" to use it in the printing loop as an array variable
i = 0

# The printing loop, for printing: The title of the article, the authour of the article and the link related to this article
for num in nameList:
    name = nameList[i]
    link = linkList[i]
    author = authorsList[i]
    i = i+1
    print("The title of the article is: ", name.get_text())
    print("The author of the article is: ", author.get_text())
    print("The link of the article is: ", link.get('href'))
    print('')

