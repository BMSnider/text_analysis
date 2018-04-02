from text_analysis.sorting.src.sorter import Sorter


class BottomUpMerge(Sorter):

    def sort(self, values: list):
        n = len(values)
        aux = []
        i = 1
        # Using a while loop instead of the for loop recommended in the book because the new value of i is dependent on
        # the previous value of i. for i in range(i, n, i) only uses the first value of i because the range is only
        # evaluated once.
        while i < n:
            for j in range(0, n - i, 2 * i):
                self.merge(values, j, j + i - 1, min(j + (2 * i) - 1, n - 1))
            i = 2 * i
