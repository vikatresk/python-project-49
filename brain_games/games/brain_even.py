import random

GAME = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 200 #максимальное число

def play():
    number = random.randint(0, MAX_NUMBER)
    question = f'{number}'
    if number%2 == 0:
        output = 'yes'
    else:
        output = 'no'
    return question, output