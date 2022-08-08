#!/usr/bin/python3
"""test file for rectangle class functionality"""


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """test instantiation, getter and setter methods"""
    

    def setUp(self):
        """set up instances"""
        self.a = Rectangle(12, 6)
        self.b = Rectangle(10, 5, 3)
        self.c = Rectangle(10, 5, 3, 4, 12)
        self.d = Rectangle(9, 5, 3, 4)

    def tearDown(self):
        """tear down all instances after each test"""
        pass

    def test_id_functionality(self):
        """test if id logic works as expected"""
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 2)
        self.assertEqual(self.c.id, 12)
        self.assertEqual(self.d.id, 3)
    
    def test_get_width(self):
        """test width getter method"""
        self.assertEqual(self.a.width, 12)
        self.assertEqual(self.b.width, 10)
        self.assertEqual(self.c.width, 10)
        self.assertEqual(self.d.width, 9)

    def test_get_height(self):
        """test height getter method"""
        self.assertEqual(self.a.height, 6)
        self.assertEqual(self.b.height, 5)
    
    def test_getter_x(self):
        """test getter for x"""
        self.assertEqual(self.a.
if __name__ == '__main__':
    unittest.main()
