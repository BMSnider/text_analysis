from text_analysis.letter_distribution.src.distribution import Distribution


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
        return value_counts

    def get_total_count(self, input_data):
        return len(input_data)

    def get_value_counts_total(self, value_counts):
        if type(value_counts) != dict:
            self.errors["totals"] = "input data for get_total_value_counts type != dict"
            return 0
        total = 0
        for i in value_counts:
            total += value_counts[i]
        return total
