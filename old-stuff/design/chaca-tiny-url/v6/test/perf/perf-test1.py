from random import randint
from sys import maxint

from bs4 import BeautifulSoup
from locust import HttpLocust, TaskSet, task

BASE_URL = 'http://dummy.host.for.this.test.cause.google.blocked.us.croaaaaaccc/?{keywords}'

chaca_tiny_urls = []
urls_map = dict()


def get_new_url():
    i = randint(0, maxint)
    keywords = 'searching+for+%d' % (i)
    return BASE_URL.replace('{keywords}', keywords)


def get_tiny_url():
    return chaca_tiny_urls[randint(0, len(chaca_tiny_urls) - 1)]


class UserBehavior(TaskSet):
    @task(1)
    def create(self):
        url = get_new_url()
        html_resp = self.client.post('/create', {'url': url})
        soup = BeautifulSoup(html_resp.content, 'html.parser')
        tiny_url = soup.find(id='tiny_url').get('href')
        urls_map[tiny_url] = url
        chaca_tiny_urls.append(tiny_url)

    @task(10)
    def redirect(self):
        if chaca_tiny_urls:
            tiny_url = get_tiny_url()
            resp = self.client.get(tiny_url, allow_redirects=False)
            if not (resp.status_code == 302 and \
                                resp.headers['Location'] == urls_map[tiny_url]):
                details = "[%d, %s]" % (resp.status_code, str(resp.headers))
                resp.failure('redirect of %s failed: %s' % (tiny_url, details))


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000
