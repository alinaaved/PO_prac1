# engine.py
def run_game(game_module):
    print("Welcome to the Brain Games!")
    try:
        name = input("May I have your name? ").encode('utf-8').decode('utf-8')
    except UnicodeDecodeError:
        name = input("May I have your name? ").encode('latin-1').decode('latin-1')

    print(f"Hello, {name}!")

    print(game_module.DESCRIPTION)

    for _ in range(3):  # Максимум 3 раунда
        question, correct_answer = game_module.generate_question()
        print(f"Question: {question}")
        try:
            user_answer = input("Your answer: ").encode('utf-8').decode('utf-8')
        except UnicodeDecodeError:
            user_answer = input("Your answer: ").encode('latin-1').decode('latin-1')

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")