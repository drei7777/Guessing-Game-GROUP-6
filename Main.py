import random

target = None
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

def evaluate(guess):
    global target  # Access the global target variable
    
    if guess < 1 or guess > 20:
        return "error", "out of range"
    elif guess < target:
        return "low", "too low"
    elif guess > target:
        return "high", "too high"
    else:
        return "win", "correct"

def guessing_game():
    # used logic from Randomizer_Vi branch
    target = random.randint(1, 20)
    attempts = 0

    print_ui()
    print("\nWelcome to the Number Guessing Game!")

    # Start the game loop
    while True:
        user_input = input("\nEnter your guess (1-20): ")
        
        # Check if the input consists only of digits
        if not user_input.isdigit():
            print("Invalid input! Please enter a valid whole number.")
            continue
            
        # Convert valid string input to integer
        guess = int(user_input)
        attempts += 1
        
        # Use the evaluate function for game logic
        status, message = evaluate(guess)
        
        if status == "error":
            print(f"Error: {message}! Please enter a number between 1 and 20.")
        elif status == "low":
            print(f"Too low! Try a higher number. ({message})")
        elif status == "high":
            print(f"Too high! Try a lower number. ({message})")
        elif status == "win":
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

# Run the game
if __name__ == "__main__":
    guessing_game()