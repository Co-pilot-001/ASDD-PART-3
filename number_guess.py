import random

def check_guess(secret_number, guess):
    if guess < secret_number:
        return "Too low!"
    elif guess > secret_number:
        return "Too high!"
    else:
        return "Correct"

def play_game():
    secret_number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            result = check_guess(secret_number, guess)

            if result == "Too low!":
                print(result + " Try again.")
            elif result == "Too high!":
                print(result + " Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_game()
