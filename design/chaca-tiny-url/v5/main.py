import webapp2

from home import HomePage
from create import CreatePage
from redirect import RedirectPage

app = webapp2.WSGIApplication([
    webapp2.Route('/', handler=HomePage, name='home', methods=['GET']),
    webapp2.Route('/<:(.+)>', handler=RedirectPage, name='redirect', methods=['GET']),
    webapp2.Route('/create', handler=CreatePage, name='create', methods=['POST'])
], debug=True)