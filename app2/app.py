# -*- coding: utf-8 -*-
import os
import pymongo
from flask import Flask

app = Flask(__name__)

@app.route("/app2/")
def home():
    # Modern Docker resolves container names via internal DNS. 
    # We fallback to 'mongo' if no explicit environment variable is set.
    db_host = os.environ.get("MONGO_HOST", "mongo")
    db_port = 27017

    # Connect to MongoDB using the MongoClient
    client = pymongo.MongoClient(db_host, db_port)
    collection = client["app2Db"]["webStats"]

    # Modern PyMongo uses update_one and explicit upsert=True keyword argument
    collection.update_one({"_id": "home"}, {"$inc": {"hit_count": 1}}, upsert=True)

    # Read the value of the hit counter
    res = collection.find_one({"_id": "home"})
    hit_count = res["hit_count"] if res else 0

    return """<h1>This is app2!</h1>
              <p>Hit Count: %d </p>
              <img src='static/images/flask-badge-2.png'/>""" % (hit_count)

if __name__ == '__main__':
    app.run()
