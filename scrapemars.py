import requests
from bs4 import BeautifulSoup
from splinter import Browser
import datetime as dt
import numpy as np
import pandas as pd
import pymongo
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

executable_path = {'executable_path':'chromedriver'}

browser = Browser('chrome', **executable_path, headless=True) 

def Scrape():


    #NASA Mars News
    page = requests.get("https://mars.nasa.gov/news/")
    soup = BeautifulSoup(page.text, 'html.parser')

    news_text = soup.find("div", "rollover_description_inner").string
    news_title = soup.find("div", "content_title", "a").contents[1].string

    #insert JPL
    page = requests.get("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
    soup = BeautifulSoup(page.text, 'html.parser')

    test = soup.find("div", class_="carousel_items").contents[1]
    item = test["style"].split("url('")
    link = item[1].split("');")[0]
    link = "https://www.jpl.nasa.gov" + link
    link

    #Mars Weather
    page = requests.get("https://twitter.com/marswxreport?lang=en")
    soup = BeautifulSoup(page.text, 'html.parser')

    tweet_text = soup.find("p", "TweetTextSize").string

    #Mars Facts
    page = requests.get("https://space-facts.com/mars/")
    soup = BeautifulSoup(page.text, 'html.parser')

    category_list = []
    facts_list = []

    categories = soup.find_all("td", "column-1")

    for item in categories:
        category_list.append(item.string)

    facts = soup.find_all("td", "column-2")

    for item in facts:
        facts_list.append(item.text.rstrip('\n'))

    mars_facts = pd.DataFrame({"description": category_list, "values": facts_list})
    mars_facts.set_index("description")
    #convert to html
    #Mars Hemispheres
    hemisphere_image_urls = []

    from splinter import Browser
    executable_path = {'executable_path':'chromedriver'}

    browser = Browser('chrome', **executable_path, headless=True)
    # Visit URL
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    #valles marineris
    button = browser.find_link_by_partial_href("valles_marineris")
    button.click()
    current_url = browser.url
    page = requests.get(current_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    image_url = soup.find(id = "wide-image").contents[3]
    title = soup.find("h2").string
    info = {"title": title, "img_url": "https://astrogeology.usgs.gov" + image_url['src']}
    hemisphere_image_urls.append(info)
    #links.append("https://astrogeology.usgs.gov" + image_url['src'])
    browser.back()

    #cerberus
    button = browser.find_link_by_partial_href("cerberus")
    button.click()
    current_url = browser.url
    page = requests.get(current_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    image_url = soup.find(id = "wide-image").contents[3]
    title = soup.find("h2").string
    info = {"title": title, "img_url": "https://astrogeology.usgs.gov" + image_url['src']}
    hemisphere_image_urls.append(info)
    browser.back()

    #schiaparelli
    button = browser.find_link_by_partial_href("schiaparelli")
    button.click()
    current_url = browser.url
    page = requests.get(current_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    image_url = soup.find(id = "wide-image").contents[3]
    title = soup.find("h2").string
    info = {"title": title, "img_url": "https://astrogeology.usgs.gov" + image_url['src']}
    hemisphere_image_urls.append(info)
    browser.back()

    #syrtis major
    button = browser.find_link_by_partial_href("syrtis_major")
    button.click()
    current_url = browser.url
    page = requests.get(current_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    image_url = soup.find(id = "wide-image").contents[3]
    title = soup.find("h2").string
    info = {"title": title, "img_url": "https://astrogeology.usgs.gov" + image_url['src']}
    hemisphere_image_urls.append(info)
    browser.quit()

    mars_dict = {"news_text": news_text, "news_title": news_title, "weather":tweet_text, "category_list": category_list,
                "featured_image": link, "facts_list": facts_list, "hemisphere_image_urls": hemisphere_image_urls}

    return mars_dict

