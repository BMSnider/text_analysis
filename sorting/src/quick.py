from random import shuffle
from src.sorter import Sorter


class Quick(Sorter):

    def sort(self, values: list):
        shuffle(values)
        self.quicksort(values, 0, len(values) - 1)

    def quicksort(self, values: list, low, hi):
        if hi <= low:
            return
        j = self.partition(values, low, hi)
        self.quicksort(values, low, j - 1)
        self.quicksort(values, j + 1, hi)
