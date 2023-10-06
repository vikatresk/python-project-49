import random


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 200  # максимальное число


def play_round():
    number = random.randint(0, MAX_NUMBER)
    question = f'{number}'
    expected_answer = 'yes' if is_even(num) is True else 'no'
    return question, expected_answer


def is_even(number):
    return number % 2 == 0
