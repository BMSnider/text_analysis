import unittest
import os
from text_analysis.file_input.src.pdf_to_string import PdfToString


class TestPdfToString(unittest.TestCase):

    def setUp(self):
        self.current_working_directory = os.getcwd()
        self.every_char_path_name = self.current_working_directory + "/pdf_to_string_test_data.pdf"
        self.test_obj = PdfToString(self.every_char_path_name)

    def test_object_type(self):
        self.assertIsInstance(self.test_obj, PdfToString)

    def test_return_type(self):
        result = self.test_obj.convert_pdf()
        self.assertIsInstance(result, str)

    def test_bad_path_name(self):
        bad_path = "fish"
        test_obj = PdfToString(bad_path)
        result = test_obj.convert_pdf()
        self.assertEqual(result, "")

    def test_password_protected(self):
        password_path = self.current_working_directory + '/pdf_password_test_data.pdf'
        test_obj = PdfToString(password_path)
        result = test_obj.convert_pdf()
        self.assertEqual(result, "")

