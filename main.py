from clownfish import Clownfish
from tang import Tang
from kong import Kong

c_fish1 = Clownfish("Laughy", 10, "Orange", "White")
t_fish1 = Tang("Dumby", 8, "Blue")
k_fish1 = Kong("Fatty", 18, "Grey")

c_fish1.get_status()
t_fish1.get_status()
k_fish1.get_status()

c_fish1.feed()
t_fish1.feed()
k_fish1.feed()

c_fish1.get_status()
t_fish1.get_status()
k_fish1.get_status()
