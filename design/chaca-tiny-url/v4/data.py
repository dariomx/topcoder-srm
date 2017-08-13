from google.appengine.ext import ndb

# this entity is to enforce uniqueness along the md5 of the url, the seq
# field is added to allow fast cross-reference with UrlRecord
class UniqueUrl(ndb.Model):
    url = ndb.StringProperty(indexed=False)
    seq = ndb.IntegerProperty(indexed=False)

# this entity is used to quickly retrieve url based on sequence (seq) associated
# to each url. this sequence is expected to be set as the id (automatically generated)
class UrlRecord(ndb.Model):
    url = ndb.StringProperty(indexed=False)
