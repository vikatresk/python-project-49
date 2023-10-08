import random
import math


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def create_round_data():
    number = random.randint(1, MAX_NUMBER)
    number1 = random.randint(1, MAX_NUMBER)
    question = f'{number} {number1}'
    expected_answer = math.gcd(number, number1)
    return (question, str(expected_answer))
