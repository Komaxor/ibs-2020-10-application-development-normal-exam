from fish import Fish


class Clownfish(Fish):

    def __init__(self, name, weight, colour, stripe_colour):
        super().__init__()
        self.name = name
        self.weight = weight
        self.colour = colour
        self.stripe_colour = stripe_colour
        self.uniqueness = "with " + self.stripe_colour + " stripes"
