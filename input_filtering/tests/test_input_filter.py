import unittest
from text_analysis.input_filtering.src.input_filter import InputFilter
from text_analysis.tools.src.input_generator import InputGenerator
from text_analysis.tools.src.timer import Timer


class TestInputFilter(unittest.TestCase):
    def setUp(self):
        input = InputGenerator()
        self.small_data = input.make_random_string(1000, "all", False)
        self.big_data = input.make_random_string(100000, "all", False)

    def test_get_characters(self):
        test = InputFilter(self.small_data)
        data = test.get_characters()
        self.assertIsInstance(data, list)

    def test_get_words(self):
        test = InputFilter(self.small_data)
        data = test.get_words()
        print(data)
        self.assertIsInstance(data, list)

    def test_get_sentences(self):
        test = InputFilter(self.small_data)
        data = test.get_sentences()
        self.assertIsInstance(data, list)

    def test_remove_char(self):
        test = InputFilter(self.small_data)
        data = test.remove_char("a")
        self.assertIsInstance(data, str)
        list_data = list(data)
        self.assertTrue("a" not in list_data)
