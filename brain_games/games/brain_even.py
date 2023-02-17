import random


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 200  # максимальное число


def play_round():
    number = random.randint(0, MAX_NUMBER)
    question = f'{number}'
    if is_even(number) is True:
        result = 'yes'
    else:
        result = 'no'
    return question, result

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
