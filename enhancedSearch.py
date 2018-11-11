#!/user/bin/python
"""
enhancedSearch.py
"""

import jsonTools as jt
import textAnalyzer as ta
from mongoBall import mongoBall

import sys,os,datetime
import json
from bson.objectid import ObjectId
import math

def usage():
    print __doc__
    sys.exit()

#enhanced search call
def enhancedSearch(searchQueryIn, mdb_collection, dict_field_name, stopwords_set):
    #figure out how this data is being inserted into the DB


    #tokenize input search
    searchQueryLen = len(searchQueryIn.split())
    searchQueryTokensList = ta.tokenize(searchQueryIn, stopwords_set)
    searchTokenFrequency = ta.termFrequency(searchQueryTokensList)
    searchRec = (ObjectId('5be8329564212212ed1dd1f0'), searchTokenFrequency)
    invertedSTF = ta.invert(searchRec)

    mdb_captions_query_format = {"caption_token_dict":1}
    mdb_query = mdb_collection.find({}, mdb_captions_query_format)
    captionTokenFrequenciesList = jt.getText(mdb_query, "caption_token_dict")


    #print captionTokenFrequenciesList[0]

    cosSimScore = {}
    STFset = set(searchTokenFrequency)
    for rec in captionTokenFrequenciesList:
        CTFset = set(rec[1])
        commonTokens = {}
        for token in STFset.intersection(CTFset):
            commonTokens.update({token:[searchTokenFrequency[token],rec[1][token]]})
        if(commonTokens):
            #print searchQueryLen
            missingTokens = searchQueryLen - len(commonTokens) * 1.0
            #print commonTokens
            #print missingTokens
            dotProd = 0.0
            a2=0.0
            b2=0.0
            for token in commonTokens:
                dotProd += commonTokens[token][0] * commonTokens[token][1]
                a2 += commonTokens[token][0] ** 2
                b2 += commonTokens[token][1] ** 2
                #print a2, commonTokens[token][0]
                #print b2, commonTokens[token][1]

            #print dotProd
            #print math.sqrt(a2)
            #print math.sqrt(b2)
            score = ((dotProd) / (math.sqrt(a2)*math.sqrt(b2)))
            if(missingTokens != 0):
                score *= (1.0/missingTokens)
            #print rec[0], score
            cosSimScore.update({rec[0] : score})

        else:
            cosSimScore.update({rec[0] : 0.0})

    mdb_query = mdb_collection.find({}, {"youtubeURL":1})
    urlScoreList = {}
    for rec in mdb_query:
        urlScoreList.update({rec["youtubeURL"] : cosSimScore[rec['_id']]})

    sortedList = sorted(urlScoreList.items(), key=lambda x: x[1], reverse=True)

    for url in sortedList:
        print url[0], url[1]

    #print commonTokens
    #print query_text



#main function setup
def main():
    #if the search query input is not given
    if (len(sys.argv)<1): usage()

    #get the search query input (This will be a file)
    #searchQueryIn = sys.argv[1]

    mdb_collection_name = "test"

    #create the mongoBall and get the collection connector
    mdb = mongoBall()
    mdb_collection = mdb.collection(mdb_collection_name)

    dict_field_name = "caption_token_dict"

    #set of stopwords
    stopwords_set = set(['all','just','being','over','both','through','yourselves','its','before','herself','had','should','to','only','under','ours','has','do','them','his','very','they','not','during','now','him','nor','did','this','she','each','further','where','few','because','doing','some','are','our','ourselves','out','what','for','while','does','above','between','t','be','we','who','were','here','hers','by','on','about','of','against','s','or','own','into','yourself','down','your','from','her','their','there','been','whom','too','themselves','was','until','more','himself','that','but','don','with','than','those','he','me','myself','these','up','will','below','can','theirs','my','and','then','is','am','it','an','as','itself','at','have','in','any','if','again','no','when','same','how','other','which','you','after','most','such','why','a','off','i','yours','so','the','having','once'])

    #Temporary
    searchQueryIn = sys.argv[1]

    #call the enhanced search
    enhancedSearch(searchQueryIn, mdb_collection, dict_field_name, stopwords_set)

if __name__ == "__main__":
    main()
