import unittest
from fibonacci import fibonacci, is_fibonacci, find_nearest_fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])

    def test_is_fibonacci(self):
        self.assertTrue(is_fibonacci(0))
        self.assertTrue(is_fibonacci(1))
        self.assertTrue(is_fibonacci(5))
        self.assertFalse(is_fibonacci(4))
        self.assertFalse(is_fibonacci(7))

    def test_find_nearest_fibonacci(self):
        self.assertEqual(find_nearest_fibonacci(4), 3)
        self.assertEqual(find_nearest_fibonacci(7), 8)
        self.assertEqual(find_nearest_fibonacci(10), 8)
        self.assertEqual(find_nearest_fibonacci(20), 21)
