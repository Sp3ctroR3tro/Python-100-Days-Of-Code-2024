import random

name_list = ["Angela", "Ben", "Chloe", "Jenny", "Michael"]

choice = random.randint(0, len(name_list) - 1)
chosen_name = name_list[choice]
print(f"{chosen_name} is going to buy the meal today!")
