import random

GAME = "What is the result of the expression?"
MAX_NUMBER = 15

def play():
    number1 = random.randint(0, MAX_NUMBER)
    operator = random.choice('+-*')
    number2 = random.randint(0, MAX_NUMBER)
    question = f'{number1 }{operator}{ number2}'
    output = ''
    if operator == '-':
        substr = number1 - number2
        output = str(substr)
    elif operator == '*':
        multipl = number1 * number2
        output = str(multipl)
    elif operator == '+':
        addition = number1 + number2
        output = str(addition)
    return question, output