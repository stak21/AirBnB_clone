#!/usr/bin/python3
"""Testing Class: place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """class to test Place."""
    def setUp(self):
        """ Sets up User for every test """
        self.place = Place()

    def test_place_for_type(self):
        """testing if place name is a string"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_empty_string(self):
        """testing string for empty string"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")

    def test_place_for_zero(self):
        """testing for zero"""
        zero = 0
        self.place = Place()
        self.assertEqual(self.place.number_rooms, zero)
        self.assertEqual(self.place.number_bathrooms, zero)
        self.assertEqual(self.place.max_guest, zero)

    def test_place_for_float(self):
        """testing for float equals 0.0"""
        zero = 0.0
        self.assertEqual(self.place.latitude, zero)
        self.assertEqual(self.place.longitude, zero)

    def test_for_empty_list(self):
        """testing for an empty list"""
        emptylist = []
        self.assertEqual(self.place.amenity_ids, emptylist)
