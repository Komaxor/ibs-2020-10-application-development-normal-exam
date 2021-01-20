class Aquarium:

    def __init__(self):
        self.fishes = set()

    def add_fish(self, fish):
        self.fishes.add(fish)

    def feed(self):
        for fish in self.fishes:
            fish.feed()

    def remove_fat_fishes(self):
        for fish in list(self.fishes):
            if fish.weight >= 11:
                self.remove_fish(fish)

    def remove_fish(self, fish):
        self.fishes.remove(fish)

    def get_status(self):
        for fish in self.fishes:
            print(fish.status())
