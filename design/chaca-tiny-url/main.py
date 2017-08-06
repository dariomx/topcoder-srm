import webapp2

URL_PARAM = 'url'

class MainPage(webapp2.RequestHandler):
    def handle_create(self, url):
        self.response.write(url)

    def handle_forward(self, id):
        self.response.write('pinche id = ' + id)

    def handle_badargs(self):
        self.response.write("either url or /id must be provided")

    def get(self, id):
        self.response.headers['Content-Type'] = 'text/plain'
        url = self.request.get(URL_PARAM).strip()
        if len(url) > 0:
            self.handle_create(url)
        elif len(id) > 0:
            self.handle_forward(id)
        else:
            self.handle_badargs()

app = webapp2.WSGIApplication([
    ('/(.*)', MainPage),
], debug=True)