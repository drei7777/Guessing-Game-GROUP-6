import random

def guessing_game():
    # 1. Generate a random secret number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")

    # 2. Start the game loop
    while True:
        # 3. Capture and validate user input
        user_input = input("Enter your guess: ")
        
        # Check if the input consists only of digits
        if not user_input.isdigit():
            print("Invalid input! Please enter a valid whole number.")
            continue
            
        # Convert valid string input to integer
        guess = int(user_input)
        attempts += 1
        
        # 4. Compare the guess to the secret number
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break

# Run the game
if __name__ == "__main__":
    guessing_game()
