import re

class InputFilter:
    def __init__(self, raw_data):
        self.data = raw_data

    def get_characters(self):
        return list(self.data)

    def get_words(self):
        """
        Returns a list of all the words contained in the data, with most
        standard English punctuation removed from the ends of each word.
        """
        L = self.data.split(" ")
        for i in range(len(L)):
            L[i] = re.sub(r"\A[.,;:\"\']+|[.,;:\"\']+\Z", "", L[i])
        return L

    def get_sentences(self):
        return self.data.split(". ")

    def remove_char(self, char):
        return self.data.replace(char, "")
