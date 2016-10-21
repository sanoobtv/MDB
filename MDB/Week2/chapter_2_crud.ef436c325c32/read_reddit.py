#!/usr/bin/env python

import json
import urllib2
import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db = connection.reddit
stories = db.stories

# drop existing collection
stories.drop()

# get the reddit home page
hdr = { 'User-Agent' : 'pymongo agent' }

req = urllib2.Request("http://www.reddit.com/r/technology/.json", headers=hdr)

reddit_page = urllib2.urlopen(req)

# parse the json into python objects
parsed = json.loads(reddit_page.read())

# iterate through every news item on the page
for item in parsed['data']['children']:
    # put it in mongo
    stories.insert_one(item['data'])
