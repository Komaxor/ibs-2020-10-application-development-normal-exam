from fish import Fish


class Tang(Fish):

    def __init__(self, name, weight, colour):
        super().__init__(name, weight, colour)
        self.uniqueness = "can suffer short-term memory loss"
        self.status = self.set_status()
