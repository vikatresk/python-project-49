from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def make_progression(start_number, end_number, step):
    progression = list(range(start_number, end_number, step))
    return progression


def create_round_data():
    start_number = randint(1, 15)
    end_number = randint(40, 60)
    step = randint(2, 4)
    progression = make_progression(start_number, end_number, step)
    missed_index = randint(0, len(progression) - 1)
    expected_answer = progression[missed_index]
    progression[missed_index] = '..'
    question = " ".join(str(i) for i in progression)
    return question, str(expected_answer)
