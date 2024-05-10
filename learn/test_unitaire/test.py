from unittest import TestCase

from main import add

class TestCalculatrice(TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(5, 10), 15)

    def test_add_with_two_letters(self):
        self.assertEqual(add("a", "b"), "ab")

    def test_add_with_two_booleans(self):
        self.assertEqual(add(True, False), 1)
        self.assertEqual(add(True, True), 2)
        self.assertEqual(add(False, False), 0)

    def test_add_with_two_none(self):
        with self.assertRaises(TypeError):
            add(None, None)

