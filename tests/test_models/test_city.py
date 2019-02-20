#!/usr/bin/python3
"""Testing Class: City"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """class to test city."""
    def setUp(self):
        """ Sets up city for every test """
        self.city = City()

    def test_city_name_string(self):
        """testing if city name is a string"""
        self.city = City()
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_city_empty_str(self):
        """testing if city name is empty string"""
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
