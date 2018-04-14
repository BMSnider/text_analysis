from text_analysis.letter_distribution.src.distribution import Distribution
from operator import itemgetter

class DistributionBuilder:

    def __init__(self):
        self.errors = {}

    def make_distribution(self, input_data):
        value_counts = self.get_value_counts(input_data)

    def get_value_counts(self, input_data):
        value_counts = {}

        for element in input_data:
            if element in value_counts:
                value_counts[element] += 1
            else:
                value_counts[element] = 1
        return self.value_counts_tuple(value_counts)

    def value_counts_tuple(self, value_counts):
        final_counts = []
        for element, count in value_counts.items():
            final_counts.append((element, count))
        return sorted(final_counts, key=itemgetter(1))

    def get_total_count(self, input_data):
        return len(input_data)

    def get_value_counts_total(self, value_counts):
        if type(value_counts) != list:
            self.errors["totals"] = "input data for get_total_value_counts type != list"
            return False
        return sum(element[1] for element in value_counts)

    def get_mode_elements(self, value_counts):
        if type(value_counts) != list:
            self.errors["mode"] = "input data for get_mode_elements type != list"
            return False

        largest_index = len(value_counts) - 1
        elements = [value_counts[largest_index][0]]
        value = value_counts[largest_index][1]

        for i in range(largest_index - 1, -1, -1):
            test_element = value_counts[i]
            if test_element[1] != value:
                break
            else:
                elements.append(test_element[0])
        return elements
