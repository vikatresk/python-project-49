import random


GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100


def play_round():
    number = random.randint(0, MAX_NUMBER)
    question = f'{number}'
    if is_prime(number):
        result = 'yes'
    else:
        result = 'no'
    return question, result


def is_prime(number):
    if number <= 1:
        return False
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number % 2
