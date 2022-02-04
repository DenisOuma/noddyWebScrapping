import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys  import Keys
from lxml import html
import re

# left some comment on every details and functionality of the webscrapping process.
browser = webdriver.Chrome('driver/chromedriver') #chrome driver installed to be use if on window the file should be in .exe formart
browser.get('https://www.linkedin.com/uas/login') #Loging in addres.
browser.maximize_window()
# Open the txt file
file = open('config.txt')
lines = file.readlines()
#getting the text by their index.
username = lines[0]
password = lines[1]

idElement = browser.find_element_by_id('username')
# send the userName information
idElement.send_keys(username)

idElement = browser.find_element_by_id('password')
# send user Password
idElement.send_keys(password)
idElement.submit() #submit Password

# serch functionality on the page
file = open('serchcontent.txt') #the text to be added on the serch link
lines = file.readlines()
search = lines[0]
browser.get('https://www.linkedin.com/search/results/companies/?keywords='+search+'&origin=GLOBAL_SEARCH_HEADER&sid=dKW') #Serch link changed
time.sleep(5) #Waiting duration


src = browser.page_source
soup = BeautifulSoup(src, 'lxml')
prime_div = soup.find('div', {'class': 'ph0 pv2 artdeco-card mb2'})
ul_list = prime_div.find('ul', {'class': 'reusable-search__entity-result-list list-style-none'})
div_name = ul_list.find_all('li',{'class': 'reusable-search__result-container'})

# A for loop to print all the Links from the serch list.
print(f"Sarch result for  "+ search.upper())
for link in range(0, len(div_name)):
    company_link = div_name[link].find('a', attrs={'href': re.compile("^https://")})
    print(f"Company Link is:" + company_link.get('href'))






