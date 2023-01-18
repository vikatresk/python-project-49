import prompt

ROUNDS = 3

def start(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.GAME)
    score = 0
    while score < ROUNDS:
        question, output = game.play()
        print(f'Question: {question}')
        reply = prompt.string('Your answer: ')
        if reply == str(output):
            print ('Correct!')
            score += 1
        else:
            print(f" '{reply}' is wrong answer ;(. Correct answer was '{output}'.")
            print(f"Let's try again, {name}.")
            score -= 1
            break
    if score == ROUNDS:
        print(f"Congratulations, {name}!")