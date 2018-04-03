import unittest
from text_analysis.letter_distribution.src.distribution_builder import DistributionBuilder
from text_analysis.letter_distribution.src.distribution import Distribution
from text_analysis.tools.input_generator import InputGenerator



class TestDistributionBuilder(unittest.TestCase):

    def setUp(self):
        input_gen = InputGenerator()
        self.test_data = input_gen.make_random_string(1000)
        self.test =
