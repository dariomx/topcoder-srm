import webapp2

from query import QueryPage

app = webapp2.WSGIApplication([
    webapp2.Route('/query', handler=QueryPage, name='query', methods=['GET']),
], debug=True)