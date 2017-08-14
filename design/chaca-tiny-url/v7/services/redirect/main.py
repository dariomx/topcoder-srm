import webapp2

from redirect import RedirectPage

app = webapp2.WSGIApplication([
    webapp2.Route('/<:(.+)>', handler=RedirectPage, name='redirect', methods=['GET']),
], debug=True)