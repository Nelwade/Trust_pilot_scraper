from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time
import pandas as pd
import numpy as np



options = webdriver.ChromeOptions()
options.headless = True # opens chrome in the background

# Launches the chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.implicitly_wait(10)

# link = "https://www.trustpilot.com/review/asos.com"

def open_parse_link(link):
    driver.get(link) # opens url
    time.sleep(5) # waits for 5 seconds to allow the page to open

    html =driver.page_source # gets the html from the page source
    soup = BeautifulSoup(html, 'html.parser') # Parses the html in the page using BEautifulSoup

    return soup

   
    # reviews = soup.find_all('div', class_='review-container')
def get_title(soup):
    title = soup.find("h1")
    title = title.text.strip("Reviews").strip()
    return title

def reviews(soup):
    store_reviews_list = []
    reviews = soup.find_all("div", class_="styles_reviewContent__0Q2Tg")

    for review in reviews[0:5]:
        #review_content = review.find("p", class_ = "typography_typography__QgicV typography_body__9UBeQ typography_color-black__5LYEn typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3").text
        review_content = review.p.text
        store_reviews_list.append(review_content)
        
    return store_reviews_list



# soup = open_parse_link(link)
# print(reviews(soup))
