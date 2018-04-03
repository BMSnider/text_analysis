import unittest
from text_analysis.letter_distribution.src.distribution_builder import DistributionBuilder
from text_analysis.letter_distribution.src.distribution import Distribution
from text_analysis.tools.input_generator import InputGenerator



class TestDistributionBuilder(unittest.TestCase):

    def setUp(self):
        input_gen = InputGenerator()
        self.test_data = input_gen.make_random_string(100000)
        self.test = DistributionBuilder()

    def test_has_property_errors(self):
        self.assertEqual(self.test.errors, {})

    def test_get_value_counts(self):
        value_counts = self.test.get_value_counts(self.test_data)
        self.assertIsInstance(value_counts, dict)
        print(value_counts)
