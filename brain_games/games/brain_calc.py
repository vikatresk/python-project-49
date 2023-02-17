import random


GAME_DESCRIPTION = "What is the result of the expression?"
MAX_NUMBER = 15


def play_round():
    number1 = random.randint(0, MAX_NUMBER)
    operator = random.choice(['+','-', '*'])
    number2 = random.randint(0, MAX_NUMBER)
    question = f'{number1 } {operator} { number2}'
    return question, connumerate(number1, number2, operator)
    
def connumerate(number1, number2, operator):
    if operator == '+':
        result = number1 + number2
    if operator == '-':
        result = number1 - number2
    if operator == '*':
        result = number1 * number2
    return result
