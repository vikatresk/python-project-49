import random


GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100


def play():
    number = random.randint(0, MAX_NUMBER)
    question = f'{number}'
    if is_prime(number):
        output = 'yes'
    else:
        output = 'no'
    return question, output


def is_prime(number):
    if number <= 1:
        return False
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number
