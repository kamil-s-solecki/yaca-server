import unittest
from utils.test_case import TestCase
from utils.socket import Socket


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

    def test_wrong_token_causes_disconnection(self):
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


if __name__ == '__main__':
    unittest.main()
