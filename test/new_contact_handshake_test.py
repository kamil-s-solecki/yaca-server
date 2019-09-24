import unittest
from utils.test_case import TestCase
from utils.api import api


class NewContactHandshakeTest(TestCase):
    def setUp(self):
        self.user_token = api.post_user(
            {'username': 'first_user'}).json()['token']

        self.other_user_token = api.post_user(
            {'username': 'second_user'}).json()['token']

    def test_creating_contact_init_token_for_invalid_user(self):
        response = api.get_contact_init_token('incorrect token').json()

        self.assertEqual("Incorrect token", response['message']['User-Token'])

    def test_creating_contact_init_token_for_valid_user(self):
        response = api.get_contact_init_token(self.user_token).json()

        self.assertNotEmptyString(response['contact_init_token'])

    def test_getting_contact_pin_for_invalid_contact_init_token(self):
        response = api.get_contact_pin(
            'incorrect token', self.other_user_token).json()

        self.assertEqual('No contact exists for given contact token',
                         response['message']['contact_init_token'])

    def test_getting_contact_pin_for_valid_contact_init_token(self):
        contact_init_token = api.get_contact_init_token(
            self.user_token).json()['contact_init_token']

        response = api.get_contact_pin(
            contact_init_token, self.other_user_token).json()

        self.assertRegex(response['pin'], r'^[0-9][0-9][0-9][0-9][0-9]$')
        self.assertEqual('first_user', response['username'])

    def test_getting_contact_pin_gives_you_a_contact_token(self):
        contact_init_token = api.get_contact_init_token(
            self.user_token).json()['contact_init_token']

        response = api.get_contact_pin(
            contact_init_token, self.other_user_token).json()

        self.assertNotEmptyString(response['contact_token'])

    def test_posting_incorrect_contact_pin(self):
        response = api.post_contact_pin('incorrect pin').json()

        self.assertEqual('No contact exists for given pin',
                         response['message']['pin'])

    def test_posting_contact_pin_returns_a_contact_token_and_username(self):
        contact_init_token = api.get_contact_init_token(
            self.user_token).json()['contact_init_token']
        get_pin_response = api.get_contact_pin(
            contact_init_token, self.other_user_token).json()

        post_pin_response = api.post_contact_pin(
            get_pin_response['pin']).json()

        self.assertEqual(get_pin_response['contact_token'],
                         post_pin_response['contact_token'])
        self.assertEqual('second_user', post_pin_response['username'])


if __name__ == '__main__':
    unittest.main()
