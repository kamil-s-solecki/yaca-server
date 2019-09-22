import unittest
from utils.test_case import TestCase
from utils.api import api
from utils.socket import Socket


class NewContactHandshakeTest(TestCase):
    def setUp(self):
        self.user_token = api.post_user(
            {'username': 'first_user'}).json()['token']
        self.other_user_token = api.post_user(
            {'username': 'first_user'}).json()['token']
        contact_init_token = api.get_contact_init_token(
            self.user_token).json()['contact_init_token']
        get_pin_response = api.get_contact_pin(
            contact_init_token, self.other_user_token).json()
        self.contact_token = api.post_contact_pin(
            get_pin_response['pin']).json()['contact_token']

        self.socket = Socket()

        def connect():
            self.socket.introduce_yourself(self.user_token)
        self.socket.on_connect(connect)

        self.other_socket = Socket()

        def connect():
            self.other_socket.introduce_yourself(self.other_user_token)
        self.other_socket.on_connect(connect)

    def test_sending_message_to_non_existing_contact(self):
        result = {}

        def on_authorized(data):
            self.socket.sio.send(
                {'contact': 'incorrect', 'message': 'not important'})
        self.socket.on_authorized(on_authorized)

        def on_incorrect_contact(data):
            result['data'] = data
            self.socket.disconnect()
        self.socket.on_incorrect_contact(on_incorrect_contact)

        self.socket.connect()

        self.assertEqual('Incorrect contact token',
                         result['data']['error'])

    def test_sending_message_to_existing_contact(self):
        result = {}

        def on_authorized(data):
            self.socket.sio.send(
                {'contact': self.contact_token, 'message': 'some message'})
            self.socket.disconnect()
        self.socket.on_authorized(on_authorized)

        def on_message(data):
            result['data'] = data
            self.other_socket.disconnect()
        self.other_socket.on_message(on_message)

        self.socket.connect(block=False)
        self.other_socket.connect()

        self.assertEqual('some message',
                         result['data']['message'])


if __name__ == '__main__':
    unittest.main()
