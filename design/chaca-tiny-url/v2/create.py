# handler logic for creating new records given an url

import hashlib
import os
from random import randint

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
URL_PARAM = "url"


def md5(url):
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


def create_record(url):
    seq = randint(0, len(ALPHABET)**8-1)
    record = (url, change_base(seq), md5(url))
    return record


class CreatePage(webapp2.RequestHandler):
    def get_tiny_url(self, id):
        return self.request.host_url + '/' + id

    def post(self):
        url = self.request.get(URL_PARAM).strip()
        if len(url) > 0:
            record = create_record(url)
            print(record)
            tiny_url = self.get_tiny_url(record[1])
            tpl = JINJA_ENVIRONMENT.get_template('html/create.html')
            tpl_values = {
                'url': url,
                'tiny_url': tiny_url
            }
            self.response.write(tpl.render(tpl_values))
        else:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write("missing parameter url")
