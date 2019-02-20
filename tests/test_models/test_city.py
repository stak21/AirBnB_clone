#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """class to test city."""
    def test_city_name_string(self):
        """testing if city name is a string"""
        self.city = City()
        self.assertEqual(type(self.city.name), str)
