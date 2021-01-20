from fish import Fish


class Kong(Fish):

    def __init__(self, name, weight, colour):
        super().__init__(name, weight, colour)
        self.weight_gain = 2
        self.uniqueness = "gains extra weight when fed"
