class Sorter:

    def exchange(self, values, i, j):
        temp = values[i]
        values[i] = values[j]
        values[j] = temp

    def merge(self, values, low, mid, hi):
        i = low
        j = mid + 1
        # copy list to another list
        aux = []
        for k in range(low, hi + 1):
            aux.append(values[k])
        for L in range(low, hi + 1):
            #iaux and jaux are shifted by low because python lists can only
            #start at index 0. Therefore, when L = low this makes the value
            #of aux[iaux] == values[low] and aux[jaux] == values[mid + 1]
            iaux = i - low
            jaux = j - low
            if i > mid:
                values[L] = aux[jaux]
                j += 1
            elif j > hi:
                values[L] = aux[iaux]
                i += 1
            elif aux[jaux] < aux[iaux]:
                values[L] = aux[jaux]
                j += 1
            else:
                values[L] = aux[iaux]
                i += 1

    def show(self, values):
        for val in values:
            print(val, end=" ")
        print()

    def is_sorted(self, values) -> bool:
        for val in range(1, len(values)):
            if values[val] < values[val - 1]:
                return False
        return True
