# games/progression.py
import random

DESCRIPTION = "What number is missing in the progression?"


def generate_progression(start, step, length):
    return [start * (step ** i) for i in range(length)]


def generate_question():
    start = random.randint(1, 5)
    step = random.randint(2, 5)
    length = random.randint(5, 10)
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer