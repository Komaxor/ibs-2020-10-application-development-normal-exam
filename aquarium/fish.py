class Fish:

    def __init__(self):
        self.name = ""
        self.weight = 0
        self.colour = ""
        self.weight_gain = 1
        self.uniqueness = ""

    def status(self):
        return (self.name + ", weight: " + str(self.weight) +
                ", colour: " + self.colour + ", " + "uniqueness: " +
                self.uniqueness)

    def feed(self):
        self.weight += self.weight_gain
