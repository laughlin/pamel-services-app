import unittest
from models.EngineModel import EngineModel

class TestStringMethods(unittest.TestCase):

    def test_isNone(self):
        freshEngineModel = EngineModel()
        self.assertTrue(freshEngineModel.engine is None)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)