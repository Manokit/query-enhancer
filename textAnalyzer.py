#!/user/bin/python
"""
textAnalyzer.py
"""

import re,sys,os
import math

FIELD_PATTERN = '^(\w+)\.*(\w*)'

def removeQuotes(string):
    """
    Removes quotation marks from an input string
    """

    return ''.join(ch for ch in string if ch != '"')


def simpleTokenize(string, split_regex=r'\W+'):
    """
    A simple implementation of input string tokenization
    """

    return filter(lambda string: string != '', re.split(split_regex, string.lower()))


def tokenize(string,stopwords_set):
    """
    An implementation of input string tokenization that excludes stopwords
    """

    return filter(lambda tokens: tokens not in stopwords_set, simpleTokenize(string))


#probably not needed
def countTokens(vendorRDD):
    """
    Count and return the number of tokens
    """

    return vendorRDD.flatMap(lambda (x,y): y).count()


def termFrequency(tokens):
    """
    Compute Term Frequency of the tokens for each video item
    """

    tf_dict = {}
    for token in tokens:
        if token in tf_dict:
            tf_dict[token] += 1
        else:
            tf_dict[token] = 1
    #return tf_dict
    tf_norm = {}
    N = len(tokens)
    for key in tf_dict.keys():
        tf_norm[key] = 1. * tf_dict[key] / N
    return tf_norm


#For cosine similarity
class cosineSimilarity(object):

    def dotprod(self,a,b):
        """
        Compute dot product
        """

        return sum([v*b[k] for (k,v) in a.items() if k in b.keys()])

    def norm(self,a):
        """
        Compute the square root of the dot product
        """

        return math.sqrt(self.dotprod(a,a))

    def cossim(self,a,b):
        """
        Compute cosine similarity
        """

        return self.dotprod(a,b) / (self.norm(a)*self.norm(b))

def invert(record):
    """
    Invert (ID, tokens) to a list of (token, ID)
    """

    id_url = record[0]
    print id_url
    weights = record[1]
    pairs = [(token, id_url) for (token, weight) in weights.items()]
    return (pairs)

def commonKeys(invRecA, invRecB):
    """
    Swap (token, (ID,URL)) to ((ID,URL), token)
    """

    tempset = set()
    for token in set(invRecA).intersection(set(invRecB)):
        #print token
        tempset.add((invRecA[token],invRecB[token]), token)

    return tempset

def grab_field_content(jsonDoc,field):
    """
    """

    match = re.search(FIELD_PATTERN, field)
    is_base_field = False
    if match.group(2) == '':
        is_base_field = True

    if is_base_field == True:
        print jsonDoc[match.group(1)]
    else:
        for thing in jsonDoc[match.group(1)]:
            print thing[match.group(2)]
