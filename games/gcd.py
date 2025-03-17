# games/gcd.py
import random
from math import gcd

DESCRIPTION = "Find the smallest common multiple of given numbers."


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_three(a, b, c):
    return lcm(lcm(a, b), c)


def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    num3 = random.randint(1, 20)
    question = f"{num1} {num2} {num3}"
    correct_answer = str(lcm_three(num1, num2, num3))
    return question, correct_answer