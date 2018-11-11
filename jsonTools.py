#!/user/bin/python
"""
jsonTools.py
"""

def parseMongoRecord(mdb_record,dict_field_name):
    """
    Expects a record containing an '_id' key, and other
    important non-selection field keys such as summary,
    details, etc.
    """
    record_id = mdb_record.pop('_id', None)
    record_dict = mdb_record[dict_field_name]
    return (record_id, record_dict)


def getText(mdb_cursor, dict_field_name):
    """
    Creates a list of (record_id,record_str) tuples from a given MongoDB query
    """
    corpus = []
    for record in mdb_cursor:
        corpus.append(parseMongoRecord(record, dict_field_name))
    return corpus
