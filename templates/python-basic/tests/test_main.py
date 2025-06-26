"""
Unit tests cho main.py
"""

import unittest
import sys
import os

# Thêm src vào Python path để import được modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import example_function
from utils import validate_input, format_output


class TestMain(unittest.TestCase):
    """Test cases cho main module"""
    
    def test_example_function(self):
        """Test function example_function"""
        result = example_function("Test")
        expected = "Xin chào, Test!"
        self.assertEqual(result, expected)
    
    def test_example_function_empty_string(self):
        """Test với empty string"""
        result = example_function("")
        expected = "Xin chào, !"
        self.assertEqual(result, expected)


class TestUtils(unittest.TestCase):
    """Test cases cho utils module"""
    
    def test_validate_input_string(self):
        """Test validate_input với string"""
        self.assertTrue(validate_input("test", str))
        self.assertTrue(validate_input("123", str))
    
    def test_validate_input_number(self):
        """Test validate_input với số"""
        self.assertTrue(validate_input("123", int))
        self.assertFalse(validate_input("abc", int))
    
    def test_format_output_list(self):
        """Test format_output với list"""
        data = [1, 2, 3]
        result = format_output(data)
        expected = "1\n2\n3"
        self.assertEqual(result, expected)
    
    def test_format_output_string(self):
        """Test format_output với string"""
        data = "Hello"
        result = format_output(data)
        self.assertEqual(result, "Hello")


if __name__ == "__main__":
    # Chạy tất cả tests
    unittest.main()
