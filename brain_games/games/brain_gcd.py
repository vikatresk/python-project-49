import random
import math

GAME = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100

def play():
    number = random.randint(1, MAX_NUMBER)
    number1 = random.randint(1, MAX_NUMBER)
    question = f'{number} {number1}'
    output = math.gcd(number, number1)
    return question, output