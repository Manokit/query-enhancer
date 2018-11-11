import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017/")

#Temporary Data
videoID = "videoID"
capt_toke_dict = {
    "key" : "value",
    "key2" : "value"
}
numVideos = 10


# Insert each document
for x in range(0, numVideos):
    test_s = {
        "youtubeURL" : "https://youtube.com/?v=" + videoID, #creates the url given the video ID (will probably change if we end up passing the url)
        "caption_token_dict" : capt_toke_dict
    }
    db = client.exampleDB
    db.test.insert(test_s)

for a in db.test.find():
    pprint.pprint(a)
