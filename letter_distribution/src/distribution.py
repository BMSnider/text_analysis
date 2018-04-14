
class Distribution:
    def __init__(self, element_type):
        self.element_type = element_type
        self.element_frequency = []
        self.count = 0
        self.most_common = ()
        self.least_common = ()
