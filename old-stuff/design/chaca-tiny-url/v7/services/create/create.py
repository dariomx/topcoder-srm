# handler for creating a new record given an url

import hashlib
import os

import jinja2
import webapp2
from google.appengine.ext import ndb

from data import UniqueUrl, UrlRecord
from encode import encode_seq

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

URL_PARAM = 'url'


def get_md5(url):
    return hashlib.md5(url).hexdigest()


def get_new_seq():
    seq = UrlRecord.allocate_ids(size=1)[0]
    assert seq is not None
    return seq


@ndb.transactional(xg=True)
def create_record(url, seq):
    md5 = get_md5(url)
    unique_rec = UniqueUrl.get_by_id(md5)
    if unique_rec:
        if url != unique_rec.url:
            raise ValueError('Unthinkable happened: md5 collision')
        seq = unique_rec.seq
    else:
        record = UrlRecord(url=url, id=seq)
        record.put()
        unique_rec = UniqueUrl(url=url, seq=seq, id=md5)
        unique_rec.put()
    return seq


class CreatePage(webapp2.RequestHandler):
    def get_tiny_url(self, seq):
        return self.request.host_url + '/' + encode_seq(seq)

    def post(self):
        url = self.request.get(URL_PARAM).strip()
        url = url.encode("ascii", "ignore")
        if len(url) > 0:
            seq = create_record(url, get_new_seq())
            tiny_url = self.get_tiny_url(seq)
            tpl = JINJA_ENVIRONMENT.get_template('html/create.html')
            tpl_values = {
                'url': url,
                'tiny_url': tiny_url
            }
            self.response.write(tpl.render(tpl_values))
        else:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Missing or invalid url parameter')
