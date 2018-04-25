import PyPDF2
from PyPDF2.utils import PdfReadError


class PdfToString:
    """Converts .pdf file to raw string."""

    def __init__(self, path):
        self.path = path

    def convert_pdf(self):
        str_file = ''
        try:
            with open(self.path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                num_pages = pdf_reader.numPages
                for page in range(num_pages):
                    page_obj = pdf_reader.getPage(page)
                    str_file += str(page_obj.extractText())
        except IOError:
            print("{} could not be converted to a string".format(self.path))
        except PdfReadError:
            print("{} is encrypted".format(self.path))
        return str_file


