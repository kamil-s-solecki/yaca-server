import unittest
from utils.test_case import TestCase
from utils.api import api


class CreateUserTest(TestCase):
    def test_creating_user_returns_a_token_and_username(self):
        data = {'username': 'foo'}

        json = api.post_user(data).json()

        self.assertNotEmptyString(json['token'])
        self.assertEqual(json['username'], 'foo')

    def test_creating_user_returns_different_token_each_time(self):
        first_response = api.post_user({'username': 'foo'}).json()

        second_response = api.post_user({'username': 'bar'}).json()

        self.assertNotEqual(first_response['token'], second_response['token'])

    def test_username_is_required(self):
        response = api.post_user({})

        self.assertEqual(400, response.status_code)
        json = response.json()
        self.assertEqual("This value cannot be blank",
                         json['message']['username'])

    def test_username_cannot_be_blank(self):
        response = api.post_user({'username': '  '})

        self.assertEqual(400, response.status_code)
        json = response.json()
        self.assertEqual("This value cannot be blank",
                         json['message']['username'])

    def test_username_cannot_be_longer_than_80_characters(self):
        response = api.post_user({'username': 'a' * 81})

        self.assertEqual(400, response.status_code)
        json = response.json()
        self.assertEqual("This value must have 80 characters or less",
                         json['message']['username'])


if __name__ == '__main__':
    unittest.main()
