import prompt


ROUNDS_TO_WIN = 3


def start(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.GAME_DESCRIPTION)
    score = 0
    while score < ROUNDS_TO_WIN:
        question, result = game.play_round()
        print(f'Question: {question}')
        reply = prompt.string('Your answer: ')
        if reply == result:
            print('Correct!')
            score += 1
        else:
            print(
                f"'{reply}' is wrong answer ;(. Correct answer was '{result}'."
            )
            print(f"Let's try again, {name}!")
            return
    if score == ROUNDS_TO_WIN:
        print(f"Congratulations, {name}!")
