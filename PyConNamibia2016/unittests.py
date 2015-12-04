import unittest
import geraints_function

class TestGeraintsFunction(unittest.TestCase):

    def test_geraints_function(self):
        self.assertEqual(geraints_function(7, 9), 2)
        self.assertEqual(geraints_function(20.4, 3.1), abs(20.4-3.1))
