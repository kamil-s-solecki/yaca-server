import requests
import re


class Api():
    def __init__(self, url):
        self.url = url

    def post(self, path, data):
        url = self._create_url(path)
        return requests.post(url, json=data)

    def _create_url(self, path):
        return re.sub(r"/$", "", self.url) + "/" + re.sub(r"^/", "", path)

    def post_user(self, data):
        return self.post('/users', data)


api = Api('http://localhost:5000/')
