import random


GAME_DESCRIPTION = "What is the result of the expression?"
MAX_NUMBER = 15


def create_round_data():
    number1 = random.randint(0, MAX_NUMBER)
    operator = random.choice(['+', '-', '*'])
    number2 = random.randint(0, MAX_NUMBER)
    question = f'{number1 } {operator} { number2}'
    expected_answer = calculate(number1, number2, operator)
    return (question, str(expected_answer))


def calculate(number1, number2, operator):
    if operator == '+':
        result = number1 + number2
    if operator == '-':
        result = number1 - number2
    if operator == '*':
        result = number1 * number2
    return result
