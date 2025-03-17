def get_player_name():
    print("Welcome to the Brain Games!")
    return input("May I have your name? ")


def play_rounds(game_module, name):
    print(game_module.DESCRIPTION)

    for _ in range(3):  
        question, correct_answer = game_module.generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return False

    return True

def run_game(game_module):
    name = get_player_name()
    print(f"Hello, {name}!")

    if play_rounds(game_module, name):
        print(f"Congratulations, {name}!")