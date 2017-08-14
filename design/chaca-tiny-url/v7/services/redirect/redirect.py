# handler for forwarding user to original url (given tiny version)

import webapp2

from data import UrlRecord
from encode import decode_seq


class RedirectPage(webapp2.RequestHandler):
    def get(self, seq_b):
        seq = decode_seq(seq_b)
        record = UrlRecord.get_by_id(seq)
        if record:
            self.redirect(str(record.url))
        else:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Non existent url: ' + str(seq))
