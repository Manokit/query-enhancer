#!/usr/bin/python
"""
mongoBall.py
A python class that stores the information needed to connect to a
Mongo database

Attributes:
    database - name of the Mongo Database (default: 'exampleDB')
    client   - name of the Mongo host client (default: 'mongodb://localhost')
    port     - port number of the Mongo Database (default: 27017)
"""

import pymongo

class mongoBall(object):

    def __init__(self,database='exampleDB',client='mongodb://localhost',port=27017,passProtected=False,userName='admin',userPass='password'):
        """ Initializes the MongoDB setup object
        Args:
            database (str or unicode): name of the Mongo database
            client (str or unicode):   name of the Mongo database client
            port (int):                port number
        """
        self.database = database
        self.client = client
        self.port = port
        self.passProtected = passProtected
        self.userName = userName
        self.userPass = userPass

    def getDatabase(self):
        """ Return the name of the Mongo Database
        """
        return self.database

    def getClient(self):
        """ Return the name of the Mongo client host
        """
        return self.client

    def getPort(self):
        """ Return the port number
        """
        return self.port

    def stat(self):
        print "Database: ",self.database
        print "Client:   ",self.client
        print "Port:     ",self.port

    def connection(self):
        """ Establish a connection to the database
        """
        return pymongo.MongoClient(self.client,self.port)

    def db(self):
        """ Get a handle to the database
        """
        mdb = getattr(self.connection(),self.database)
        if self.passProtected == True:
            mdb.authenticate(self.userName,self.userPass)
        return mdb

    def collection(self, collection):
        """ Access collection 'collection'
        """
        return getattr(self.db(),collection)
