from google.appengine.ext import ndb

# this entity is used for enforcing uniqueness (based on key retrieval)
# it's key is expected to be md5 of the url, and the seq field is added
# to allow fast cross-reference with UrlRecord
class UniqueUrl(ndb.Model):
    url = ndb.StringProperty(indexed=False)
    seq = ndb.StringProperty(indexed=False)

# this is the actual data: associates a sequence with each url
# (from where a short version of it can be built, but we just save
# the sequence). the sequence (seq) is not mentioned cause is
# expected to be the key (same as md5 for UniqueUrl entity)
class UrlRecord(ndb.Model):
    url = ndb.StringProperty(indexed=False)
