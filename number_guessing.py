import random
import time

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have a limited number of chances to guess the correct number.")

def select_difficulty():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        return 10
    elif choice == 2:
        return 5
    elif choice == 3:
        return 3
    else:
        print("Invalid choice. Defaulting to Medium difficulty.")
        return 5

def provide_hint(number, guess):
    difference = abs(number - guess)
    if difference <= 10:
        return "You're very close!"
    elif difference <= 20:
        return "You're close!"
    else:
        return "You're far off."

def play_game():
    welcome_message()
    chances = select_difficulty()
    number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()
    while chances > 0:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess == number:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            print(f"It took you {elapsed_time:.2f} seconds.")
            return attempts
        else:
            hint = provide_hint(number, guess)
            if guess < number:
                print(f"{hint} Try guessing higher.")
            else:
                print(f"{hint} Try guessing lower.")
        chances -= 1
        print(f"You have {chances} chances left.")
    print(f"Sorry, you've run out of chances. The correct number was {number}.")
    return None

def main():
    high_score = None
    while True:
        attempts = play_game()
        if attempts is not None:
            if high_score is None or attempts < high_score:
                high_score = attempts
                print(f"New high score: {high_score} attempts!")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thank you for playing the Number Guessing Game!")

if __name__ == "__main__":
    main()