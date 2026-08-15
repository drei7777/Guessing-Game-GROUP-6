#UI part
def print_ui():
    width = 40
    print("+" + "-" * width + "+")
    print("|" + " " * width + "|")
    print("|" + "I'm thinking of a number".center(width) + "|")
    print("|" + "between 1 to 20".center(width) + "|")
    print("|" + "now guess the number.".center(width) + "|")
    print("|" + " " * width + "|")
    print("+" + "-" * width + "+")

#GAME LOGIC/RANDOMAYSIRRR
from random import randint

target = randint(1, 20)
def evaluate(guess):
    if guess < 1 or guess > 20:
        return "error", "out of range"
    elif guess < target:
        return "low", "too low"
    elif guess > target:
        return "high", "too high"
    else:
        return "win", "correct"