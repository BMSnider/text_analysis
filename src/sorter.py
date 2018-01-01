class Sorter:

    def exchange(self, values: list, i, j):
        for val in range(len(values)):
            temp = values[i]
            values[i] = values[j]
            values[j] = temp

    def show(self, values: list):
        for val in values:
            print(val, end=" ")
        print()

    def is_sorted(self, values: list) -> bool:
        for val in range(1, len(values)):
            if values[val] > values[val - 1]:
                return False
        return True
