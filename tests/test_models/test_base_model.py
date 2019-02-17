#/usr/bin/python3
from models.base_model import BaseModel
import unittest

class TestBase(unittest.TestCase):
    """ Testing implementation of class: BaseModel """
    def test_init(self):
        self.base = BaseModel()
