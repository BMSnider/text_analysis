from sorting.src.sorter import Sorter


class Insertion(Sorter):

    def sort(self, values: list):
        for i in range(1, len(values)):
            j = i
            while j > 0 and values[j] < values[j-1]:
                self.exchange(values, j, j - 1)
                j -= 1
