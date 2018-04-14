from text_analysis.letter_distribution.src.distribution import Distribution
from operator import itemgetter


class DistributionBuilder:

    def __init__(self):
        self.errors = {}

    def make_distribution(self, element_type,  input_data):
        dist = Distribution(element_type)
        dist.element_frequency = self.get_element_frequency(input_data)
        dist.count = self.get_total_count(input_data)
        dist.most_common = self.get_mode_elements(dist.element_frequency)
        dist.least_common = self.get_least_common_elements(dist.element_frequency)
        return dist

    def get_element_frequency(self, input_data):
        element_frequency = {}

        for element in input_data:
            if element in element_frequency:
                element_frequency[element] += 1
            else:
                element_frequency[element] = 1
        return self.frequency_tuple(element_frequency)

    def frequency_tuple(self, element_frequency):
        final_counts = []
        for element, count in element_frequency.items():
            final_counts.append((element, count))
        return sorted(final_counts, key=itemgetter(1))

    def get_total_count(self, input_data):
        return len(input_data)

    def get_element_frequency_total(self, element_frequency):
        if type(element_frequency) != list:
            self.errors["totals"] = "input data for get_total_value_counts type != list"
            return False
        return sum(element[1] for element in element_frequency)

    def get_mode_elements(self, element_frequency):
        if type(element_frequency) != list:
            self.errors["mode"] = "input data for get_mode_elements type != list"
            return False

        largest_index = len(element_frequency) - 1
        elements = [element_frequency[largest_index][0]]
        value = element_frequency[largest_index][1]

        for i in range(largest_index - 1, -1, -1):
            test_element = element_frequency[i]
            if test_element[1] != value:
                break
            else:
                elements.append(test_element[0])
        return elements, value

    def get_least_common_elements(self, element_frequency):
        if type(element_frequency) != list:
            self.errors["least common"] = "input data for get_least_common_elements type != list"
            return False

        elements = [element_frequency[0][0]]
        value = element_frequency[0][1]

        for i in range(1, len(element_frequency)):
            test_element = element_frequency[i]
            if test_element != value:
                break
            else:
                elements.append(test_element[0])
        return elements, value
