#!usr/bin/python3
""" Test BaseModel """
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test cases for the BaseModel """
    def setUp(self):
        self.base = BaseModel()

    def test_id(self):
        """ Test if id equals a string """
        self.assertEqual(type(self.base.id), str)

    def test_id_len(self):
        """ Test the length of id """
        self.assertEqual(len(self.base.id), 36)

    @unittest.expectedFailure
    def test_id_unique(self):
        """ Test if the each instance of base id is unique """
        self.base1 = BaseModel()
        self.assertEqual(self.base.id, self.base1.id)

    def test_created_at_instance_of(self):
        """ Test the variable createdat is an instance of date time """
        self.assertTrue(isinstance(self.base.created_at, datetime))

    def test_updated_at_instance_of(self):
        """ Test the variable updated_at is an instance of date time"""
        self.assertTrue(isinstance(self.base.updated_at, datetime))

    def test_updated_at(self):
        """ Test the variable updated_at """
        self.base.save()
        self.assertTrue(self.base.created_at != self.base.updated_at)

    def test_str(self):
        """ Test the __str__ """
        shoji = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(self.base.__str__(), shoji)

    def test_to_dict_return(self):
        """ Test to_dict: return value"""
        test_dict = self.base.to_dict()
        self.assertTrue(type(test_dict) is dict)

    def test_to_dict_dunder(self):
        """ Test the return dunder of __dict__ """
        dunder = self.base.__dict__
        for attr in dunder.keys():
            self.assertNotIn('__', attr)

    def test_to_dict_class(self):
        """ Test if __class__ was added into the dictionary """
        test_dict = self.base.to_dict()
        self.assertTrue('__class__' in test_dict)

    def test_to_dict_new_attr(self):
        """ Test a new attr to the object """
        self.base.chicken = 1
        test_dict = self.base.to_dict()
        self.assertTrue('chicken' in test_dict)

    def test_to_dict_updated_at(self):
        """ Test if updated_at is a string inside of the dictionary """
        test_dict = self.base.to_dict()
        self.assertEqual(type(test_dict['updated_at']), str)

    def test_to_dict_created_at(self):
        """ Test if created_at is a string inside of the dictionary """
        test_dict = self.base.to_dict()
        self.assertEqual(type(test_dict['created_at']), str)

    def test_save(self):
        """Test save, if date is datetime object"""
        self.save_test = BaseModel()
        before = self.save_test.updated_at
        self.save_test.save()
        after = self.save_test.updated_at
        self.assertTrue(type(after) is datetime)
        """Test save if strings are the same"""
        before = str(before)
        after = str(after)
        self.assertFalse(after == before)
