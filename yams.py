predefined_rolls = [
    [6, 6, 6, 6, 6],  # Yams 0
    [4, 4, 4, 4, 2],  # Carré 1
    [3, 3, 3, 2, 2],  # Full 2
    [1, 2, 3, 4, 6],  # Petite Suite 3
    [2, 3, 4, 5, 1],  # Petite Suite 4
    [1, 2, 3, 4, 5],  # Grande Suite 5
    [2, 3, 4, 5, 6],  # Grande Suite 6
    [2, 2, 2, 4, 5],  # Brelan 7
    [1, 3, 4, 5, 6],  # Chance 8
    [1, 2, 2, 4, 5],  # Non gagnant 9
    [1, 3, 4, 4, 6],  # Non gagnant 10
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
            return 1
    return 0

def is_carre(dice_roll):
    for die in set(dice_roll):
        if dice_roll.count(die) >= 4:
            return 1
    return 0
def is_full(dice_roll):
    dice_count = {die: dice_roll.count(die) for die in set(dice_roll)}
    return 3 in dice_count.values() and 2 in dice_count.values()

def is_grande_suite(dice_roll):
    sorted_roll = sorted(dice_roll)
    return sorted_roll == [1, 2, 3, 4, 5] or sorted_roll == [2, 3, 4, 5, 6]

def is_chance(dice_roll):
    return sum(dice_roll)