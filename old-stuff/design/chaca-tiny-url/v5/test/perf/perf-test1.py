from random import randint
from sys import maxint

from bs4 import BeautifulSoup
from locust import HttpLocust, TaskSet, task

BASE_URL = 'https://www.google.com.mx/search?site=&source=hp&q={keywords}&oq={keywords}&gs_l=psy-ab.3...5203.6650.0.6848.0.0.0.0.0.0.0.0..0.0....0...1.1.64.psy-ab..0.0.0.MWhkwKGKR3Y'

chaca_tiny_urls = []
urls_map = dict()


def get_new_url():
    i = randint(0, maxint)
    keywords = 'searching+for+%d' % (i)
    return BASE_URL.replace('{keywords}', keywords)


def get_tiny_url():
    return chaca_tiny_urls[randint(0, len(chaca_tiny_urls) - 1)]


class UserBehavior(TaskSet):
    def check_redirect(self, tiny_url):
        with self.client.get(tiny_url, catch_response=True) as resp:
            if len(resp.history) == 0:
                resp.failure('redirect of %s failed: %s' % (tiny_url))
            else:
                resp = resp.history[0]
                if not (resp.status_code == 302 and \
                                    resp.headers['Location'] == urls_map[tiny_url]):
                    details = "[%d, %s]" % (resp.status_code, str(resp.headers))
                    resp.failure('redirect of %s failed: %s' % (tiny_url, details))

    @task(1)
    def create(self):
        self.client.get('/')
        url = get_new_url()
        html_resp = self.client.post('/create', {'url': url})
        soup = BeautifulSoup(html_resp.content, 'html.parser')
        tiny_url = soup.find(id='tiny_url').get('href')
        urls_map[tiny_url] = url
        chaca_tiny_urls.append(tiny_url)
        self.check_redirect(tiny_url)

    @task(1)
    def redirect(self):
        if chaca_tiny_urls:
            self.check_redirect(get_tiny_url())


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000
