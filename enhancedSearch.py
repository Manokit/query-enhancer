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

def usage():
    print __doc__
    sys.exit()

#enhanced search call
def enhancedSearch(searchQueryIn, mdb_collection, dict_field_name, stopwords_set):
    #figure out how this data is being inserted into the DB

    #tokenize input search
    searchQueryTokensList = ta.tokenize(searchQueryIn, stopwords_set)
    searchTokenFrequency = ta.termFrequency(searchQueryTokensList)
    searchRec = (ObjectId('5be8329564212212ed1dd1f0'), searchTokenFrequency)
    invertedSTF = ta.invert(searchRec)
    print invertedSTF

    mdb_captions_query_format = {"caption_token_dict":1}
    mdb_query = mdb_collection.find({}, mdb_captions_query_format)
    captionTokenFrequenciesList = jt.getText(mdb_query, "caption_token_dict")


    #print captionTokenFrequenciesList[0]
    for rec in captionTokenFrequenciesList:
        invertedCTF = ta.invert(rec)
        print invertedCTF
        #print ta.commonKeys(invertedSTF, invertedCTF)

    a=[]
    for tokens in invertedSTF:
        a.append(searchTokenFrequency[token])
        b.append(caption)

    ta.cosineSimilarity().cossim()

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
