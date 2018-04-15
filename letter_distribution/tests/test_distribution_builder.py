import unittest
from text_analysis.letter_distribution.src.distribution_builder import DistributionBuilder
from text_analysis.letter_distribution.src.distribution import Distribution
from text_analysis.tools.src.input_generator import InputGenerator
from text_analysis.tools.src.timer import Timer


class TestDistributionBuilder(unittest.TestCase):

    def setUp(self):
        input_gen = InputGenerator()
        self.big_test_data = input_gen.make_random_string_list(1000000)
        self.small_test_data = input_gen.make_random_string_list(27)
        self.test = DistributionBuilder()

    def test_has_property_errors(self):
        self.assertEqual(self.test.errors, {})

    def test_get_value_counts(self):
        value_counts = self.test.get_element_frequency(self.small_test_data)
        self.assertIsInstance(value_counts, list)

    def test_total_method(self):
        small_timer_len = Timer("small_data_len")
        small_timer_loop = Timer("small_data_loop")
        big_timer_len = Timer("big_data_len")
        big_timer_loop = Timer("big_data_loop")

        small_timer_len.start()
        small_total_len = self.test.get_total_count(self.small_test_data)
        small_timer_len.stop()

        small_loop_value_counts = self.test.get_element_frequency(self.small_test_data)
        small_timer_loop.start()
        small_total_loop = self.test.get_element_frequency_total(small_loop_value_counts)
        small_timer_loop.stop()

        big_timer_len.start()
        big_total_len = self.test.get_total_count(self.big_test_data)
        big_timer_len.stop()

        big_loop_value_counts = self.test.get_element_frequency(self.big_test_data)
        big_timer_loop.start()
        big_total_loop = self.test.get_element_frequency_total(big_loop_value_counts)
        big_timer_loop.stop()

        self.assertEqual(len(self.small_test_data), small_total_len)
        self.assertEqual(len(self.small_test_data), small_total_loop)
        self.assertEqual(len(self.big_test_data), big_total_len)
        self.assertEqual(len(self.big_test_data), big_total_loop)

        print(small_timer_len.formatted_time())
        print(small_timer_loop.formatted_time())
        print(big_timer_len.formatted_time())
        print(big_timer_loop.formatted_time())

        small_len_faster = small_timer_len.duration() < small_timer_loop.duration()
        self.assertTrue(small_len_faster)

        big_len_faster = big_timer_len.duration() < big_timer_loop.duration()
        self.assertTrue(big_len_faster)

    def test_get_mode_elements(self):
        value_counts = self.test.get_element_frequency(self.big_test_data)
        mode_elements = self.test.get_mode_elements(value_counts)

        self.assertIsInstance(mode_elements, tuple)
        print("value_counts")
        print(value_counts)
        print("mode_elements")
        print(mode_elements)

    def test_get_least_common_elements(self):
        value_counts = self.test.get_element_frequency(self.big_test_data)
        mode_elements = self.test.get_least_common_elements(value_counts)

        self.assertIsInstance(mode_elements, tuple)
        print("value_counts")
        print(value_counts)
        print("least_common_elements")
        print(mode_elements)

    def test_make_distribution(self):
        element_type = "letter"
        dist = self.test.make_distribution(element_type, self.small_test_data)
        self.assertIsInstance(dist, Distribution)

        timer = Timer("big data distribution creation")
        timer.start()
        big_dist = self.test.make_distribution(element_type, self.big_test_data)
        timer.stop()
        print(timer.formatted_time())