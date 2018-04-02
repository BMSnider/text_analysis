import unittest
from text_analysis.letter_distribution.src.letter_distribution import LetterDistribution
from text_analysis.sorting.src.input_generator import InputGenerator

class TestLetterDistribution(unittest.TestCase):

    def setUp(self):
        test_input = InputGenerator()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        number = test_input.make_random_number(26)
        self.test_data = {}

        self.sum = 0
        for i in range(26):
            self.test_data[alphabet[i]] = number[i]
            self.sum += number[i]
        self.test = LetterDistribution(self.test_data)

    def test_has_property_count(self):
        self.assertEqual(self.test.count, self.sum)
