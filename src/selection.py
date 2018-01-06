from src.sorter import Sorter


class Selection(Sorter):

    def sort(self, values):
        for i in range(len(values)):
            min = i
            for j in range(i + 1, len(values)):
                if values[j] < values[min]:
                    min = j
            self.exchange(values, i, min)
