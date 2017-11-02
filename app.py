import requests
from bs4 import BeautifulSoup
from splinter import Browser
import datetime as dt
import numpy as np
import pandas as pd
import pymongo

from flask import Flask, jsonify, render_template, request

import scrapemars

conn = "mongodb://admin:password@ds143245.mlab.com:43245/heroku_2xxf76ft"
client = pymongo.MongoClient(conn)

db = client.mars_scrape_db

app = Flask(__name__)

@app.route("/")
#change to route that passes data to html
def welcome():
    #queries
    #mars_database = db.mars.find()
    for doc in db.mars.find():
        news_1 = doc["news_text"].strip()
        news_2 = doc["news_title"].strip()
        weather_1 = doc["weather"]
        featured_image = doc["featured_image"]
        #categories
        category_1 = doc["category_list"][0]
        category_2 = doc["category_list"][1]
        category_3 = doc["category_list"][2]
        category_4 = doc["category_list"][3]
        category_5 = doc["category_list"][4]
        category_6 = doc["category_list"][5]
        category_7 = doc["category_list"][6]
        category_8 = doc["category_list"][7]
        category_9 = doc["category_list"][8]
        #facts
        fact_1 = doc["facts_list"][0]
        fact_2 = doc["facts_list"][1]
        fact_3 = doc["facts_list"][2]
        fact_4 = doc["facts_list"][3]
        fact_5 = doc["facts_list"][4]
        fact_6 = doc["facts_list"][5]
        fact_7 = doc["facts_list"][6]
        fact_8 = doc["facts_list"][7]
        fact_9 = doc["facts_list"][8]
        #images
        hemi_image_1_title = doc["hemisphere_image_urls"][0]["title"]
        hemi_image_2_title = doc["hemisphere_image_urls"][1]["title"]
        hemi_image_3_title = doc["hemisphere_image_urls"][2]["title"]
        hemi_image_4_title = doc["hemisphere_image_urls"][3]["title"]
        hemi_image_1_link = doc["hemisphere_image_urls"][0]["img_url"]
        hemi_image_2_link = doc["hemisphere_image_urls"][1]["img_url"]
        hemi_image_3_link = doc["hemisphere_image_urls"][2]["img_url"]
        hemi_image_4_link = doc["hemisphere_image_urls"][3]["img_url"]

    return render_template("index.html", news_text=news_1, news_title=news_2, weather=weather_1, feat_image=featured_image,
                            description_1=category_1, description_2=category_2,description_3=category_3,description_4=category_4,description_5=category_5,
                            description_6=category_6,description_7=category_7,description_8=category_8,description_9=category_9,
                            value_1=fact_1, value_2=fact_2, value_3=fact_3, value_4=fact_4, value_5=fact_5, value_6=fact_6, value_7=fact_7, 
                            value_8=fact_8, value_9=fact_9, image_1_title=hemi_image_1_title, image_2_title=hemi_image_2_title, image_3_title=hemi_image_3_title, image_4_title=hemi_image_4_title, 
                            image_1_link=hemi_image_1_link, image_2_link=hemi_image_2_link, image_3_link=hemi_image_3_link, image_4_link=hemi_image_4_link)
    #, news_2=news_title, categories=category_list, facts=facts_list, hemi_pictures=hemisphere_image_urls)

@app.route("/scrape")
def data_retrieval():
    var = scrapemars.Scrape()
    db.mars.insert(var)

    return  (
        welcome()
    )

if __name__ == '__main__':
    app.run(debug=True)