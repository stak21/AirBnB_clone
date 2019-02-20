#!/usr/bin/python3
"""Testing Class: Review test"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """class to test review."""

    def setUp(self):
        """ Sets up User for every test """
        self.review = Review()

    def test_if_str(self):
        """test if type is str"""
        self.assertEqual(type(self.review.place_id), str)

    def test_empty_string(self):
        """testing string for empty string"""
        self.assertEqual(self.review.user_id, "")
