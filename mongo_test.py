import pymongo

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.mars_scrape_db

#news_text = db.mars.find({})["news_text"]

for doc in db.mars.find():
    print(doc["news_text"].strip())
    print(doc["news_title"].strip())
    print(doc["category_list"])
    print(doc["facts_list"])
    print(doc["hemisphere_image_urls"])

print(db.mars["news_text"])