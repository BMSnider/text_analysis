from sorting.src.sorter import Sorter


class Shell(Sorter):

    def sort(self, values: list):
        N = len(values)
        h = 1

        while h < N/3:
            h = 3 * h + 1
        while h >= 1:
            for i in range(h, N):
                j = i
                while j >= h and values[j] < values[j - h]:
                    self.exchange(values, j, j - h)
                    j -= h
            h = h // 3
