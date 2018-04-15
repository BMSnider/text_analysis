from random import randint, choice
# static functions that return lists containing random strings or ints


class InputGenerator:

    def make_random_string(self, length, charset="alpha", lowercase=True):
        char_options = {"alpha": "abcdefghijklmnopqrstuvwxyz",
                        "alphaspace": "abcdefghijklmnopqrstuvwxyz ",
                        "alphanumeric": "abcdefghijklmnopqrstuvwxyz 1234567890",
                        "all": "abcdefghijklmnopqrstuvwxyz 1234567890-=`\][;'/.,~!@#$%^&*()_+|}{:\"?><"}
        if charset in char_options.keys():
            chars = char_options[charset]
        else:
            return ""
        result = ""
        for i in range(length):
            randindex = randint(0, len(chars) - 1)
            if choice([True, False]):
                result += chars[randindex]
            else:
                result += chars[randindex].upper()
        return result

    def make_random_number(self, length):
        result = ""
        for i in range(length):
            result += str(randint(0, 9))
        return result

    def make_random_string_list(self, length):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        result = []
        for i in range(length):
            randindex = randint(0, len(alphabet) - 1)
            result.append(alphabet[randindex])
        return result

    def make_random_number_list(self, length):
        result = []
        for i in range(length):
            result.append(randint(0, 9))
        return result
