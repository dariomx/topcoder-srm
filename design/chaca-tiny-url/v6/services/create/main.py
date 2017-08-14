import webapp2

from create import CreatePage

app = webapp2.WSGIApplication([
    webapp2.Route('/create', handler=CreatePage, name='create', methods=['POST'])
], debug=True)