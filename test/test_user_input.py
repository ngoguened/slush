"""
Unit Testing
"""
import unittest
from hypothesis import given
from hypothesis.strategies import text
from src.user_input import UserInput

class TestUserInput(unittest.TestCase):
    """Testing the user input class"""
    @given(text(min_size=1, max_size=100))
    def test_valid_input(self, test_input):
        """Test that valid input is accepted"""
        user_input = UserInput(test_input)
        self.assertEqual(user_input(), test_input)

    @given(text(max_size=0))
    def test_input_not_empty(self, test_input):
        """Test that empty input raises a ValueError"""
        with self.assertRaises(ValueError):
            UserInput(test_input)

    @given(text(min_size=101))
    def test_input_less_than_100_chars(self, test_input):
        """Test that input greater than 100 characters raises a ValueError"""
        with self.assertRaises(ValueError):
            UserInput(test_input)
