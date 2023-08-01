import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_my_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([]), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 1, 4), [2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 1, -1), [2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -3, -1), [3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -3, 4), [3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 10), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -10), [1, 2, 3, 4, 5])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 1, 10), [2, 3, 4, 5])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 1, -10), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 2, None), [3, 4, 5])
        self.assertEqual(arrs.my_slice("Hello, world!", 2, -2), "llo, worl")
        self.assertEqual(arrs.my_slice((1, 2, 3, 4, 5), 1, 4), (2, 3, 4))
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 2, 5), [3, 4, 5])
        with self.assertRaises(TypeError):
            arrs.my_slice(12345, 1, 4)