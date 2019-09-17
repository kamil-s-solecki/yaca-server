import unittest
from utils.test_case import TestCase
from utils.socket import Socket
from utils.api import api


class SeflIntroductionTest(TestCase):
    def test_can_connect(self):
        connection_established = {'success': False}
        socket = Socket()

        def connect():
            connection_established['success'] = True
            socket.disconnect()
        socket.on_connect(connect)

        socket.connect()

        self.assertTrue(connection_established['success'])

    def test_wrong_token_causes_incorrect_token_event(self):
        socket = Socket()
        error = {}

        def connect():
            socket.introduce_yourself('dummy token')
        socket.on_connect(connect)

        def on_incorrect_token(data):
            error['message'] = data['message']
            socket.disconnect()
        socket.on('incorrect_token', on_incorrect_token)

        socket.connect()

        self.assertEqual('Incorrect token', error['message'])

    def test_correct_token_causes_authorized_event(self):
        socket = Socket()
        result = {'event_emmited': False}
        token = api.post_user(
            {'username': 'introduction_test_user'}).json()['token']

        def connect():
            socket.introduce_yourself(token)
        socket.on_connect(connect)

        def on_authorized(data):
            result['event_emmited'] = True
            socket.disconnect()
        socket.on('authorized', on_authorized)

        socket.connect()

        self.assertTrue(result['event_emmited'])


if __name__ == '__main__':
    unittest.main()
