# handler for forwarding user to original url (given tiny version)

import webapp2
from google.appengine.ext import ndb

from data import UrlRecord
from encode import decode_seq


class RedirectPage(webapp2.RequestHandler):
    def get(self, seq_b):
        seq = decode_seq(seq_b)
        key = ndb.Key(UrlRecord, seq)
        record = key.get()
        if record:
            self.redirect(str(record.url))
        else:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Non existent url: ' + str(seq))
