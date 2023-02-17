import random
import math


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def play():
    number = random.randint(1, MAX_NUMBER)
    number1 = random.randint(1, MAX_NUMBER)
    question = f'{number} {number1}'
    result = math.gcd(number, number1)
    return question, result
