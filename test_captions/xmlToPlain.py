#!/user/bin/python
"""
xmlToPlain.py
"""
import re
from xml.sax.saxutils import unescape
import requests

# Set up the parameters we want to pass to the API.
parameters = {"v": "2yFCyPX3kT0", "lang": "en"}

# call the api
response = requests.get("https://www.youtube.com/api/timedtext?", params=parameters)
print response.content

def parseCaptions(youtube_url):
    # f = open (r'/Users/zaffre/Documents/CS/sunhacks2018/sunhacks-2018-project/parsing/pleasework.txt')
    # s = f.read()
    text = re.sub('<[^>]+>', '', s)

    data=text.replace('\n', ' ').rihueplace('.', '').replace('!', '').replace('?', '')

    data = unescape(data, {"&#39;": "'", "&quot;": '"'})

    f = open("parsed_test_output.txt", "w")
    f.write(data)
    f.close()


def main(youtube_url):
    captions_string = ""
    youtube_url, captions_string = parseCaptions(youtube_url)
    print "youtube_url: " + youtube_url
    print "caption_string: " + captions_string
    return()

import requests
response = requests.get("http://video.google.com/timedtext?v=2yFCyPX3kT0&type=track&lang=en")
s = response.content
parsed = parseCaptions(text)
print(parsed)