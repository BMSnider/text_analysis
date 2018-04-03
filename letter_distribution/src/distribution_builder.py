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
