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