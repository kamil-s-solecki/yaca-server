import requests
import re


class Api():
    def __init__(self, url):
        self.url = url

    def post(self, path, data=None, user_token=None):
        url = self._create_url(path)
        headers = {}
        if user_token:
            headers['User-Token'] = user_token
        return requests.post(url, json=data, headers=headers)

    def get(self, path, data=None, user_token=None):
        url = self._create_url(path)
        headers = {}
        if user_token:
            headers['User-Token'] = user_token
        return requests.get(url, params=data, headers=headers)

    def post_user(self, data):
        return self.post('/users', data)

    def get_contact_init_token(self, user_token):
        return self.get('/contacts/tokens/init', user_token=user_token)

    def get_contact_pin(self, contact_init_token, user_token):
        return self.get('/contacts/pins',
                        {'contact_init_token': contact_init_token},
                        user_token=user_token)

    def post_contact_pin(self, pin):
        return self.post('/contacts/pins',
                         {'pin': pin})

    def _create_url(self, path):
        return re.sub(r"/$", "", self.url) + "/" + re.sub(r"^/", "", path)


api = Api('http://localhost:5000/')
