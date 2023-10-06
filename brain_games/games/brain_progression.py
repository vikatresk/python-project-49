from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'
START_NUMBER = randint(1, 15)  # initial number
END_NUMBER = randint(40, 60)  # end number
STEP = randint(2, 4)  # progression step
LENGTH = randint(5, 10)  # amount of numbers


def make_progression(start_number, end_number, step):
    progression = list(range(start_number, end_number, step))[:LENGTH]
    return progression


def play_round():
    progression = make_progression(START_NUMBER, END_NUMBER, STEP)
    index = randint(0, len(progression) - 1)
    expected_answer = progression[index]
    progression[index] = '..'
    question = " ".join(str(i) for i in progression)
    return question, str(expected_answer)
