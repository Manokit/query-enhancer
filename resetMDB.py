#!/usr/bin/python
"""
resetMDB.py
"""

from mongoBall import mongoBall

mdb = mongoBall()

mdb_collection_name = "test"

mdb_collection = mdb.collection(mdb_collection_name)

for rec in mdb_collection.find({}):
    record_id = rec.pop('_id', None)
    print record_id
    print rec["caption_token_dict"]

mdb_collection.delete_many({})

for rec in mdb_collection.find({}):
    record_id = rec.pop('_id', None)
    print record_id
    print rec["caption_token_dict"]
