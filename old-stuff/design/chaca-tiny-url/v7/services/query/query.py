# handler for query service (list existing data)
# "fusil" from https://github.com/zdenulo/gae-ndb-pagination/

import os

import jinja2
import webapp2
from google.appengine.datastore.datastore_query import Cursor

from data import UniqueUrl

ITEMS = 100

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def cursor_pagination(cls, prev_cursor_str, next_cursor_str):
    if not prev_cursor_str and not next_cursor_str:
        objects, next_cursor, more = cls.query().order(cls.seq).fetch_page(ITEMS)
        prev_cursor_str = ''
        if next_cursor:
            next_cursor_str = next_cursor.urlsafe()
        else:
            next_cursor_str = ''
        next_ = True if more else False
        prev = False
    elif next_cursor_str:
        cursor = Cursor(urlsafe=next_cursor_str)
        objects, next_cursor, more = cls.query().order(cls.seq).fetch_page(ITEMS, start_cursor=cursor)
        prev_cursor_str = next_cursor_str
        next_cursor_str = next_cursor.urlsafe()
        prev = True
        next_ = True if more else False
    elif prev_cursor_str:
        cursor = Cursor(urlsafe=prev_cursor_str)
        objects, next_cursor, more = cls.query().order(-cls.seq).fetch_page(ITEMS, start_cursor=cursor)
        objects.reverse()
        next_cursor_str = prev_cursor_str
        prev_cursor_str = next_cursor.urlsafe()
        prev = True if more else False
        next_ = True

    return {'objects': objects, 'next_cursor': next_cursor_str, 'prev_cursor': prev_cursor_str, 'prev': prev,
            'next': next_}


class QueryPage(webapp2.RequestHandler):
    def get(self):
        prev_cursor = self.request.get('prev_cursor', '')
        next_cursor = self.request.get('next_cursor', '')
        res = cursor_pagination(UniqueUrl, prev_cursor, next_cursor)
        template = JINJA_ENVIRONMENT.get_template('html/query.html')
        self.response.write(template.render(res))
