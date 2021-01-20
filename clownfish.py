from fish import Fish


class Clownfish(Fish):

    def __init__(self, name, weight, colour, stripe_colour):
        super().__init__(name, weight, colour)
        self.stripe_colour = stripe_colour
        self.uniqueness = "striped with " + self.stripe_colour
