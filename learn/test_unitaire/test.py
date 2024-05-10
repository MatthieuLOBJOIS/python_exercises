from unittest import TestCase

from main import add

class TestCalculatrice(TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(5, 10), 15)