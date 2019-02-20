#!/usr/bin/python3
"""Testing class: Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """class to test amenity."""

    def setUp(self):
        """ Sets up Amenity for every test """
        self.amenity = Amenity()

    def test_amenity_name_string(self):
        """testing if amenity name is a string"""
        self.amenity = Amenity()
        self.assertEqual(type(self.amenity.name), str)

    def test_amenity_empty_str(self):
        """testing if amenity name is empty string"""
        self.amenity = Amenity
        self.assertEqual(self.amenity.name, "")
