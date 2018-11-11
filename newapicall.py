#!/usr/bin/python
"""
newapicall.py
"""

from youtube_transcript_api import YouTubeTranscriptApi
import textAnalyzer as ta
from mongoBall import mongoBall

# takes a youtube url, grabs the captions associated with the video, strips the
# captions of punctuation and special characters, and appends the captions
# into a single string
def processTranscript(youtubeUrl):
    """
    takes a youtube url, grabs the captions associated with the video, strips
    the captions of punctuation and special characters, and appends the captions
    into a single string
    """

    videoID = youtubeUrl.split('v=')[1] #splits the url and selects the video id
    jsonDoc = YouTubeTranscriptApi.get_transcript(videoID)

    captionsString = ""

    for captionText in jsonDoc:
        captionsString += ' ' + captionText.get('text')

    return(captionsString)



def main():
    """
    Setting up a list of youtube videos to demo
    """

    #mongoDB connection
    mdb = mongoBall()
    mdb_collection = mdb.collection("test")

    #empty the collection
    mdb_collection.delete_many({})
    print "Emptying Collection"

    #list of stopwords (common words such as: "the", "a", "of", etc.)
    stopwords_set = set(['all','just','being','over','both','through','yourselves','its','before','herself','had','should','to','only','under','ours','has','do','them','his','very','they','not','during','now','him','nor','did','this','she','each','further','where','few','because','doing','some','are','our','ourselves','out','what','for','while','does','above','between','t','be','we','who','were','here','hers','by','on','about','of','against','s','or','own','into','yourself','down','your','from','her','their','there','been','whom','too','themselves','was','until','more','himself','that','but','don','with','than','those','he','me','myself','these','up','will','below','can','theirs','my','and','then','is','am','it','an','as','itself','at','have','in','any','if','again','no','when','same','how','other','which','you','after','most','such','why','a','off','i','yours','so','the','having','once'])

    #list of videos for the demonstration
    videoList = ["https://www.youtube.com/watch?v=GS_VcLRmCoI", "https://www.youtube.com/watch?v=g6eB8IeX_cs", "https://www.youtube.com/watch?v=FvY1fYxKFJU", "https://www.youtube.com/watch?v=DaG-y2tFBFE", "https://www.youtube.com/watch?v=JRl1FhIBeKc", "https://www.youtube.com/watch?v=DPNz6reMVXY", "https://www.youtube.com/watch?v=OvrYfsr4UDI", "https://www.youtube.com/watch?v=LOEXAn9Hj20", "https://www.youtube.com/watch?v=w525cY5FP7k"]

    for video in videoList:
        captionsString = processTranscript(video)

        captionTokensList = ta.tokenize(captionsString, stopwords_set)
        captionTokenFrequency = ta.termFrequency(captionTokensList)

        #create the mongoDB record to be inserted into the database
        mongoDBCaptionRecord = {
            "youtubeURL" : video,
            "caption_token_dict" : captionTokenFrequency
        }

        #insert the record into the MongoDB collection
        mdb_collection.insert(mongoDBCaptionRecord)

    for rec in mdb_collection.find({}):
        print rec

    print "len(videoList): %i" % (len(videoList))

if __name__ == '__main__':
    main()
