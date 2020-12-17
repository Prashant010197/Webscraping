# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 01:36:55 2020

@author: hp
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from requests import get
import time
from time import sleep
import pandas as pd
from random import randint
import simpleaudio as sa

name=[]
number_of_reviews=[]
storage_hardware=[]
ratings=[]
price=[]

link='https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=764c59f3-e646-4171-a842-6fb38dd79995&p%5B%5D=facets.price_range.from%3D13000&p%5B%5D=facets.price_range.to%3D25000'
response=get(link)
print(response.text[:500])
html_soup=soup(response.text,'html.parser')
type(html_soup)

driver=webdriver.Chrome('C:\Webdriver\chromedriver')
for i in range(2):
    sleep(randint(8,15))
    driver.get(link)
    response=get(link)
    html_soup=soup(response.text,'html.parser')
    phone_container=html_soup.find_all('div', class_='_3pLy-c row')
    for container in phone_container:
        nametext=container.find('div', {'class': '_4rR01T'}).text
        ratingtext=container.find('div', {'class': '_3LWZlK'}).text
        hardwaretext=container.find('ul', {'class': '_1xgFaf'}).text
        reviewstext=container.find('span', {'class': '_2_R_DZ'}).text
        pricetext=container.find('div', {'class': '_30jeq3 _1_WHN1'}).text
        name.append(nametext)
        ratings.append(ratingtext)
        storage_hardware.append(hardwaretext)
        number_of_reviews.append(reviewstext)
        price.append(pricetext)
    try:
        driver.find_element_by_link_text("NEXT").click()
        link=driver.current_url
    except NoSuchElementException:
        pass
wave_obj = sa.WaveObject.from_wave_file("alert.wav")
play_obj = wave_obj.play()

df = pd.DataFrame(list(zip(name, ratings, storage_hardware, number_of_reviews, price)), columns =['Name', 'Ratings', 'Hardware','Number_of_Reviews', 'Price']) 
df.to_excel('Flipkart webscrapped.xlsx')