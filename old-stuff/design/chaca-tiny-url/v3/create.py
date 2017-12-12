# handler for creating a new record given an url

import hashlib
import os
from random import randint

import jinja2
import webapp2
from google.appengine.ext import ndb

from data import UniqueUrl, UrlRecord

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
LEN_UID = 8
URL_PARAM = "url"


def get_md5(url):
    return hashlib.md5(url).hexdigest()


def change_base(n):
    base = len(ALPHABET)
    n_b = []
    rem = n
    while rem > base:
        n_b.append(ALPHABET[rem % base])
        rem = rem / base
    if rem > 0:
        n_b.append(ALPHABET[rem])
    return ''.join(n_b)

@ndb.transactional(xg=True)
def create_record(url):
    md5 = get_md5(url)
    key = ndb.Key(UniqueUrl, md5)
    unique_rec = key.get()
    if unique_rec:
        if url != unique_rec.url:
            raise ValueError("Unthinkable happened: md5 collision")
        seq = unique_rec.seq
    else:
        seq = change_base(randint(0, len(ALPHABET) ** LEN_UID - 1))
        unique_rec = UniqueUrl(url=url, seq=seq, id=md5)
        record = UrlRecord(url=url, id=seq)
        unique_rec.put()
        record.put()
    return seq


class CreatePage(webapp2.RequestHandler):
    def get_tiny_url(self, seq):
        return self.request.host_url + '/' + str(seq)

    def post(self):
        url = self.request.get(URL_PARAM).strip()
        if len(url) > 0:
            seq = create_record(url)
            tiny_url = self.get_tiny_url(seq)
            tpl = JINJA_ENVIRONMENT.get_template('html/create.html')
            tpl_values = {
                'url': url,
                'tiny_url': tiny_url
            }
            self.response.write(tpl.render(tpl_values))
        else:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write("Missing url parameter")
