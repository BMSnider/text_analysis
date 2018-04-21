import unittest
import os
from text_analysis.file_input.src.text_to_string import TextToString


class TestTextToString(unittest.TestCase):

    def setUp(self):
        current_working_directory = os.getcwd()
        self.every_char_path_name = current_working_directory + "/text_to_string_test_data.txt"
        self.test_obj = TextToString(self.every_char_path_name)

    def test_object_type(self):
        self.assertIsInstance(self.test_obj, TextToString)

    def test_return_type(self):
        result = self.test_obj.convert_txt()
        self.assertIsInstance(result, str)

    def test_bad_path_name(self):
        bad_path = "fish"
        test_obj = TextToString(bad_path)
        result = test_obj.convert_txt()
        self.assertEqual(result, "")
        
    def test_convert_txt(self):

        result = self.test_obj.convert_txt()
        data_copied_from_txt = """`1234567890 -=qwertyuiop[]\\
asdfghjkl;'zxcvbnm,./~!@#$%

^&*()_+QWERTYUIOP{}|ASDFGHJK
    L:"ZXCVBNM<>?"""
        self.assertEqual(result, data_copied_from_txt)
