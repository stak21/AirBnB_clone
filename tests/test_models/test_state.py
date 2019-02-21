#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class to test State"""
    def test_string(self):
        """test if state name is an empty string."""
        self.state = State()
        self.assertEqual(type(self.state.name), str)
        self.assertEqual(self.state.name, "")
