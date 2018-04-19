class TextToString:
    """Converts .txt file to raw string."""
    
    def __init__(self, path):
        """Takes in file and creates formatted namedtuple"""
        self.path = path

    def convert_txt(self):
        str_file = ''
        with open(self.path, "r") as txt_file:       
            for line in txt_file:
                str_file += str(line)        
    
        return str_file
