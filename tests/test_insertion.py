import unittest
from sorting.src.input_generator import InputGenerator
from sorting.src.insertion import Insertion


class TestSelection(unittest.TestCase):

    def setUp(self):
        test_input = InputGenerator()
        self.int_data = test_input.make_random_number(100)
        self.str_data = test_input.make_random_string(1000)
        self.test = Insertion()

    def test_selection_creation(self):
        self.assertIsInstance(self.test, Insertion)

    def test_int_sort(self):
        int_test = []
        for j in self.int_data:
            int_test.append(j)
        self.test.sort(int_test)
        self.assertEqual(len(self.int_data), len(int_test))
        for i in range(len(int_test)):
            self.assertTrue(self.int_data[i] in int_test)
        print(self.int_data)
        print(int_test)
        self.assertTrue(self.test.is_sorted(int_test))

    def test_str_sort(self):
        str_test = []
        for k in self.str_data:
            str_test.append(k)
        self.test.sort(str_test)
        self.assertEqual(len(self.str_data), len(str_test))
        for i in range(len(str_test)):
            self.assertTrue(self.str_data[i] in str_test)
        print(self.str_data)
        print(str_test)


if __name__ == '__main__':
    unittest.main()
