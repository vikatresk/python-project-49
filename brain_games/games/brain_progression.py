import random

GAME = 'What number is missing in the progression?'

def play():
    start_number = random.randint(1, 50)
    end_number = random.randint(50, 100)
    length = random.randint (5, 10)
    step = random.randint(1, 10)
    listing = list(range(start_number, end_number, step))
    progression = listing[:length]
    random_number = random.choice(progression)
    index = progression.index(random_number)
    output = str(random_number)
    progression[index] = ' .. '
    question = ' '.join(map(str, progression))
    return question, output