#!/usr/bin/python3
""" Testing Class: User """
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ Tests user """

    def setUp(self):
        """ Sets up User for every test """
        self.user = User()

    def test_user_testing_attributes(self):
        """ Test user attributes for string check """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_user_testing_empty(self):
        """ Test if the user Attributes are an empty string """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
