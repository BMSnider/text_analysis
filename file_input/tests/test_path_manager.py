import unittest
import os
from text_analysis.file_input.src.path_manager import PathManager
from text_analysis.file_input.src.text_to_string import TextToString


class TestPathManager(unittest.TestCase):
    def setUp(self):
        self.test_dir_path = os.getcwd()
        self.test_file_path = self.test_dir_path + "/text_to_string_test_data.txt"

    def test_get_files_dir_input(self):
        test = PathManager(self.test_dir_path)
        result = test.get_files()
        expected_file_names = ["test_path_manager.py", "test_text_to_string.py", "text_to_string_test_data.txt"]
        expected = []
        for i in expected_file_names:
            expected.append(self.test_dir_path + "/" + i)

        ordered_expected = sorted(expected)
        ordered_result = sorted(result)

        self.assertEqual(ordered_expected, ordered_result)

    def test_get_files_file_input(self):
        test = PathManager(self.test_file_path)
        result = test.get_files()
        self.assertEqual([self.test_file_path], result)

    def test_get_file_converter(self):
        test = PathManager(self.test_file_path)
        converter = test.get_file_converter(self.test_file_path)
        self.assertIsInstance(converter, TextToString)

    def test_get_file_converter_failure(self):
        test = PathManager(self.test_file_path)
        converter = test.get_file_converter("fish.fsx")
        self.assertIsNone(converter)
