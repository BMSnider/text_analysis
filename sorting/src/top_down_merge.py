from src.sorter import Sorter


class TopDownMerge(Sorter):

    def sort(self, values: list):
        self.merge_sort(values, 0, len(values) - 1)

    def merge_sort(self, values: list, low, hi):
        if hi <= low:
            return
        mid = low + (hi - low)//2
        self.merge_sort(values, low, mid)
        self.merge_sort(values, mid + 1, hi)
        self.merge(values, low, mid, hi)
