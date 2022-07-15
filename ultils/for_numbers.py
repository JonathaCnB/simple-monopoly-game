import random


def play_dice() -> int:
    dice = random.randint(1, 6)
    return dice


def random_between(start: int, end: int) -> int:
    random_value = random.randrange(start, end)
    return random_value
