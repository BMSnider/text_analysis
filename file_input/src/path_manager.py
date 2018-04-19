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

    def convert_path(self):
        """Converts path to list of files"""
        files = []
        if os.path.isdir(self.path):
            for i in os.listdir(self.path):
                # ignores subdirectories from list of files
                file_path = self.path + "/{}".format(i)
                if os.path.isfile(file_path):
                    files.append(file_path)
        elif os.path.isfile(self.path):
            files.append(self.path)
        else:
            print("{} is not recognized as a valid path".format(self.path))
        return files

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
