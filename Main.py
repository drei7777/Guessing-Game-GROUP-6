#UI part
ef print_ui():
    width = 40
    print("+" + "-" * width + "+")
    print("|" + "-" * width + "|")
    print("|" + "-" * "I'm thinking of a number".center(width) + "|")
    print("|" + "-" * "between 1 to 20".(width) + "|")
    print("|" + "-" * "now guess the number.".(width) + "|")
    print("|" + "-" * width + "|")
    print("+" + "-" * width + "+")

#GAME LOGIC/RANDOMAYSIRRR
from random import randint

target = randint(1, 20)
def eveluate(guess):
    if guess < 1 or guess > 20:
        return{"status": "error", "message:" "out of range"}
    elif guess < target:
        return{"status": "low", "message:" "too low"}
    elif guess > target:
        return{"status": "high", "message:" "too high"}
    else:
        return{"status": "win", "message:" "correct"}