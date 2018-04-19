import os
import collections

class TextToString:
    """Converts .txt file to raw string.
        
    return format is a namedtuple (path, file, raw_string)
        ex: converted_txt = TextToString(some_path).convert_txt()
            converted_txt.path will return path of file
            converted_txt.file will return file name
            converted_.raw_string will return string
    ***WILL RAISE TypeError is file in not .txt***
    """
    
    def __init__(self, path):
        """Takes in file and formats named tuple"""
        self.path = path
        self.converted_string = collections.namedtuple('converted_string', 'path file raw_string')

    def convert_txt(self):
        """converts .txt file to raw string"""
        if not self.path.endswith('.txt'): #filters non .txt files out
            raise TypeError('{}: is not recognized as a .txt file'.format(self.path))
        
        str_file = ''
        with open(self.path, "r") as txt_file:       
            for line in txt_file:
                str_file += str(line)        
    
        return self.format_output(str_file)
    
    def format_output(self, str_file):
        """Creates named tuple with format of (path, file name, string)"""
        file = os.path.basename(self.path)
        raw_string = str_file.encode("unicode-escape")
        tuple_format = self.converted_string(path = self.path, file = file, raw_string = raw_string)
        
        return tuple_format
