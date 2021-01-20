from fish import Fish


class Tang(Fish):

    def __init__(self, name, weight, colour):
        super().__init__()
        self.name = name
        self.weight = weight
        self.colour = colour
        self.uniqueness = "can suffer short-term memory loss"
