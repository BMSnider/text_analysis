import unittest
from text_analysis.letter_distribution.src.distribution import Distribution
from text_analysis.tools.src.input_generator import InputGenerator


class TestDistribution(unittest.TestCase):

    def setUp(self):
        test_input = InputGenerator()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        number = test_input.make_random_number_list(26)
        self.test_data = {}

        self.sum = 0
        for i in range(26):
            self.test_data[alphabet[i]] = number[i]
            self.sum += number[i]
        self.test = Distribution(self.test_data)

    def test_has_distribution(self):
        self.assertEqual(self.test_data, self.test.distribution)

    def test_has_property_count(self):
        self.assertEqual(self.test.count, 0)

    def test_has_property_most_common(self):
        self.assertEqual(self.test.most_common, {})

    def test_has_property_least_common(self):
        self.assertEqual(self.test.least_common, {})
