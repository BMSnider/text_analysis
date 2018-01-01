import unittest

from sorting.src.selection import Selection


class TestSelection(unittest.TestCase):
    def test_selection_creation(self):
        test = Selection()
        self.assertIsInstance(test, Selection)


if __name__ == '__main__':
    unittest.main()
