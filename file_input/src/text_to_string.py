class TextToString:
    """Converts .txt file to raw string."""
    
    def __init__(self, path):
        self.path = path

    def convert_txt(self):
        str_file = ''
        try:
            with open(self.path, "r") as txt_file:
                for line in txt_file:
                    str_file += str(line)
        except IOError:
            print("{} could not be converted to a string".format(self.path))
    
        return str_file
