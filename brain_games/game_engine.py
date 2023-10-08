import prompt


ROUNDS_TO_WIN = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_DESCRIPTION)
    for round in range(ROUNDS_TO_WIN):
        question, expected_answer = game.create_round_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != expected_answer:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{expected_answer}".\n'
                  f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')
