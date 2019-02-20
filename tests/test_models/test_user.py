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

    def test_user_testing_wrong_type(self):
        """ Test if a modified variable's value is a string """
        with self.assertRaises(TypeError):
            self.user.email = 1
        with self.assertRaises(TypeError):
            self.user.password = 1
        with self.assertRaises(TypeError):
            self.user.first_name = 1
        with self.assertRaises(TypeError):
            self.user.last_name = 1

    def test_user_update(self):
        """ Test values when user attributes are updated """
        user.first_name = "Angie"
        user.last_name = "Delgado"
        user.email = "angie@holby.com"
        user.password = "root"
        user.save()


