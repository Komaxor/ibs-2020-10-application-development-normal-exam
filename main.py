from aquarium import Aquarium
from clownfish import Clownfish
from tang import Tang
from kong import Kong

aquarium = Aquarium()

clownfish_1 = Clownfish("Laughy", 9, "orange", "white")
tong_1 = Tang("Dumby", 8, "blue")
kong_1 = Kong("Fatty", 18, "grey")

aquarium.add_fish(clownfish_1)
aquarium.add_fish(tong_1)
aquarium.add_fish(kong_1)

aquarium.get_status()

aquarium.feed()

aquarium.remove_fat_fishes()

aquarium.get_status()

aquarium.feed()

aquarium.remove_fat_fishes()

aquarium.get_status()
