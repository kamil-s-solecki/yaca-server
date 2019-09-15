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


if __name__ == '__main__':
    unittest.main()
