import random


GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa
MAX_NUMBER = 100


def play_round():
    random_number = random.randint(0, MAX_NUMBER)
    expected_answer = 'yes' if is_prime(random_number) else 'no'
    question = f'{random_number}'
    return question, str(expected_answer)


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
