from aquarium import Aquarium
from clownfish import Clownfish
from tang import Tang
from kong import Kong

aquarium = Aquarium()

# checking what happens with empty aquarium
aquarium.get_status()
aquarium.feed()
aquarium.remove_fat_fishes()

# creating fishes
clownfish_1 = Clownfish("Laughy", 9, "orange", "white")
tong_1 = Tang("Dumby", 7, "blue")
kong_1 = Kong("Fatty", 18, "grey")

# adding fishes to the aquarium
aquarium.add_fish(clownfish_1)
aquarium.add_fish(tong_1)
aquarium.add_fish(kong_1)

# testing


def test_feeding():
    print("# feeding the aquarium:")
    aquarium.feed()
    print_status()


def test_removing():
    print("# removing fat fishes:")
    aquarium.remove_fat_fishes()
    print_status()


def print_status():
    aquarium.get_status()


print("# Aquarium with fishes:")
print_status()

test_feeding()

test_removing()

test_feeding()
test_feeding()

test_removing()
