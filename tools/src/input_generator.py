from random import randint
# static functions that return lists containing random strings or ints


class InputGenerator:

    def make_random_string(self, length):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        result = []
        for i in range(length):
            randindex = randint(0, len(alphabet) - 1)
            result.append(alphabet[randindex])
        return result

    def make_random_number(self, length):
        result = []
        for i in range(length):
            result.append(randint(0, 9))
        return result
