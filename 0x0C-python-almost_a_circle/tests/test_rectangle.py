#!/usr/bin/python3
"""Unitest"""


from models.base import Base
from models.rectangle import Rectangle
import unittest
import io
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """Test case"""
    def test_init(self):
        """test the type"""
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_invalid_width(self):
        """Test the invalide width"""
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_invalide_height(self):
        """Test invalide height"""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2)

    def test_invalid_x(self):
        """Test invalide x """
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2)

    def test_invalide_y(self):
        """Test invalide y """
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3)

    def test_area(self):
        """Test the area"""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """Test the display"""
        rect = Rectangle(3, 2, 1, 1)
        expected_output = "\n ###\n ###\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """Str test"""
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/3 - 5/10")

    def test_update(self):
        """Update test"""
        rect = Rectangle(5, 10)
        rect.update(6, 12, 3, 4, 2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 2)

    def test_to_dictionary(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(rect.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
