class InputFilter:
    def __init__(self, raw_data):
        self.data = raw_data

    def get_characters(self):
        return list(self.data)

    def get_words(self):
        return self.data.split(" ")

    def get_sentences(self):
        return self.data.split(". ")

    def remove_char(self, char):
        return self.data.replace(char, "")
