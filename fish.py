class Fish:

    def __init__(self, name, weight, colour):
        self.name = name
        self.weight = weight
        self.colour = colour
        self.weight_gain = 1
        self.uniqueness = ""
        self.status = (self.name + ", weight: " + str(self.weight) +
                       ", colour: " + self.colour + ", " + "uniqueness: " +
                       self.uniqueness)

    def get_status(self):
        print(self.status)

    def feed(self):
        print(self.weight)
        print(self.weight_gain)
        self.weight += self.weight_gain
        print('yummy')
        print(self.weight)
