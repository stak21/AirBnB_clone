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
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    def test_empty_string(self):
        """testing string for empty string"""
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.text, "")
