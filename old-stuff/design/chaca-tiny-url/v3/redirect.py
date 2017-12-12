# handler for forwarding user to original url (given tiny version)

import webapp2
from google.appengine.ext import ndb

from data import UrlRecord


class RedirectPage(webapp2.RequestHandler):
    def get(self, seq):
        key = ndb.Key(UrlRecord, seq)
        record = key.get()
        if record:
            self.redirect(str(record.url))
        else:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write("Invalid url")
