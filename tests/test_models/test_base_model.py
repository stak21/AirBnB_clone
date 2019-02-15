#/usr/bin/python3
from models.base_model import BaseModel
import unittest

TEST_UUIDS = ['uuid_{}'.format(i) for i in range(10000)]

def uuid_prefix(prefix: str):
    return patch.object(uuid, 'uuid4', side_effect=['{}_{}'.format(prefix, x)
        for x in TEST_UUIDS])

class TestBase(unittest.TestCase):
    """ Testing implementation of class: BaseModel """
    @patch.object(uuid, 'uuid4', side_effect=TEST_UUIDS)
    def test_init(self):
        self.base = BaseModel()
        with uuid_prefix('obj_a'):

