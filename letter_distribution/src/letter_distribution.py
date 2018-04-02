
class LetterDistribution:
    def __init__(self, distribution):
        self.distribution = distribution
        self.count = self.get_count()

    def get_count(self):
        sum = 0
        for letter, count in self.distribution.items():
            sum += count
        return sum

