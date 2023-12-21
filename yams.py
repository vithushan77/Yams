predefined_rolls = [
    [6, 6, 6, 6, 6],  # Yams
    [4, 4, 4, 4, 2],  # Carré
    [3, 3, 3, 2, 2],  # Full
    [1, 2, 3, 4, 6],  # Petite Suite
    [2, 3, 4, 5, 1],  # Petite Suite
    [1, 2, 3, 4, 5],  # Grande Suite
    [2, 3, 4, 5, 6],  # Grande Suite
    [2, 2, 2, 4, 5],  # Brelan
    [1, 3, 4, 5, 6],  # Chance
    [1, 2, 2, 4, 5],  # Non gagnant
    [1, 3, 4, 4, 6],  # Non gagnant
]



def roll_dice(roll_number):
    return predefined_rolls[roll_number]
def is_yams(dice_roll):
    if len(set(dice_roll)) == 1:
        return 50
    return 0

def is_brelan(dice_roll):
    for die in set(dice_roll):
        if dice_roll.count(die) >= 3:
            return 28
    return 0

def is_carre(dice_roll):
    for die in set(dice_roll):
        if dice_roll.count(die) >= 4:
            return 35
    return 0
def is_full(dice_roll):
    dice_count = {die: dice_roll.count(die) for die in set(dice_roll)}
    if 3 in dice_count.values() and 2 in dice_count.values():
        return 30
    return 0

def is_grande_suite(dice_roll):
    sorted_roll = sorted(dice_roll)
    if sorted_roll == [1, 2, 3, 4, 5] or sorted_roll == [2, 3, 4, 5, 6]:
        return 40
    return 0

def is_chance(dice_roll):
    return sum(dice_roll)