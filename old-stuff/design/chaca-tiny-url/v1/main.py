import webapp2

app = webapp2.WSGIApplication([
    webapp2.Route('/', handler=home_handler, name="home", methods=['GET'])
], debug=True)