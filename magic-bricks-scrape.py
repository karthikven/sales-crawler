"""
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Chennai').text
soup = BeautifulSoup(html_text, "lxml")
builders = soup.find_all('div', class_='mb-srp__card__ads--name')
builders_list = []
for builder in builders:
	builders_list.append(builder.text)
print(builders_list)

"""

import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys

builder_list = []


browser.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Chennai")
time.sleep(1)

elem = browser.find_element("tag name","body")

no_of_pagedowns = 30

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    no_of_pagedowns-=1

post_elems = browser.find_elements("class name","mb-srp__card__ads--name")


for post in post_elems:
    builder_list.append(post.text)




with open('builders-list.txt', 'w') as f:
    for line in builder_list:
        f.write(line)
        f.write('\n')





