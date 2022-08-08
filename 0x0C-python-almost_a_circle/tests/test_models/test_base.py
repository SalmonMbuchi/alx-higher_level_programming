#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """test the super class functionality"""
    
    def test_instantiation(self):
        inst_1 = Base()
        inst_2 = Base()
        inst_3 = Base(45)
        inst_3 = Base()

        self.assertEqual(print(inst_1.id), 1)
        self.assertEqual(print(inst_2.id), 2)
        self.assertEqual(print(inst_3.id), 45)
        self.assertEqual(print(inst_4.id), 3)

if __name__ == '__main__':
    unittest.main()
