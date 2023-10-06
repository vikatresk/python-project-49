import prompt


ROUNDS_TO_WIN = 3


def start(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.GAME_DESCRIPTION)
    rounds = 0
    while rounds < ROUNDS_TO_WIN:
        question, expected_answer = game.play_round()
        print(f'Question: {question}')
        reply = prompt.string('Your answer: ')
        if reply == expected_answer:
            print('Correct!')
            rounds += 1
        else:
            print(
                f"'{reply}' is wrong answer ;(. Correct answer was '{result}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
