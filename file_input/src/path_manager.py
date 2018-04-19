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
        files = self.get_files()
        converted_files = []
        for file in files:
            converter = self.get_file_converter(file)
            data = converter.convert_txt()
            output = self.format_output(file, data)
            converted_files.append(output)
        return converted_files

    def get_files(self):
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

    def format_output(self, file_path, data):
        """Creates named tuple with format of (path, file name, string)"""
        file_name = os.path.basename(file_path)
        raw_string = data.encode("unicode-escape")
        converted_string = collections.namedtuple('converted_string', 'path file raw_string')
        return converted_string(path=self.path, file=file_name, raw_string=raw_string)
