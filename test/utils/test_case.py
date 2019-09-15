import unittest


class TestCase(unittest.TestCase):
    def assertNotEmptyString(self, value):
        self.assertEqual(str, type(value))
        self.assertTrue(bool(value))
