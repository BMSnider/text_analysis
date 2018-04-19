import os
import collections
from text_analysis.file_input.src.text_to_string import TextToString


class PathManager:
    """ Path to formatted namedtuple

    Uses FileToString classes to convert file
    or directory paths to formatted namedtuples
    with raw text data as strings and the path
    information preserved.
    """

    def __init__(self, path):  # directory or file
        self.path = path
        self.output = []

    def get_file_converter(self, file_path):

        file_converters = {".txt": TextToString
                           }
        extension = os.path.splitext(file_path)[1]

        try:
            return file_converters[extension](file_path)

        except KeyError:
            print("unsupported file extension: {}".format(extension))
            return None
            # This should probably eventually be refactored to
            # return an exception or a dummy converter
