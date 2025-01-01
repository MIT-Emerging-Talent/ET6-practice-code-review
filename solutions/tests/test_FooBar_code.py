import unittest

from ..FooBar_code import FooBar_code


class TestFooBar(unittest.TestCase):
    def test_int(self):
        self.assertEqual(
            FooBar_code(12), [1, 2, 3, "foo", 5, "Bar", 7, "foo", 9, 10, 11, "FooBar"]
        )
