import random

def random_element_exclude(lst, exclude):
    choice = random.choice(lst)
    while choice == exclude:
        choice = random.choice(lst)
    return choice