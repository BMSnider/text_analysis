import unittest
import os
from text_analysis.file_input.src.text_to_string import TextToString


class TestTextToString(unittest.TestCase):

    def setUp(self):
        current_working_directory = os.getcwd()
        self.every_char_path_name = current_working_directory + "/text_to_string_test_data.txt"

    def test_object_type(self):
        test_obj = TextToString(self.every_char_path_name)
        self.assertIsInstance(test_obj, TextToString)

    def test_convert_txt(self):

        test_obj = TextToString(self.every_char_path_name)
        result = test_obj.convert_txt()
        data_copied_from_txt = """`1234567890 -=qwertyuiop[]\\
asdfghjkl;'zxcvbnm,./~!@#$%

^&*()_+QWERTYUIOP{}|ASDFGHJK
    L:"ZXCVBNM<>?"""
        self.assertEqual(result, data_copied_from_txt)
