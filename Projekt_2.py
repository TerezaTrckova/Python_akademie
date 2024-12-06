"""
projekt_2.py: Druhý projekt do Engeto Online Python Akademie
author: Tereza Trčková
email: terda.trckova@seznam.cz
discord: tereza_trckova
"""

import random
import time

def generate_secret_number():
    """Generates a random 4-digit number with unique digits, not starting with 0."""
    while True:
        number = random.randint(1000, 9999)
        if len(set(str(number))) == 4:
            return str(number)

def is_valid_guess(guess):
    """Checks if the user's guess is valid."""
    if len(guess) != 4:
        return False, "Your guess must be exactly 4 digits."
    if not guess.isdigit():
        return False, "Your guess must contain only digits."
    if guess[0] == "0":
        return False, "Your guess cannot start with 0."
    if len(set(guess)) != 4:
        return False, "Your guess must not contain duplicate digits."
    return True, ""

def evaluate_guess(secret, guess):
    """Evaluates the user's guess and returns the counts of bulls and cows."""
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def main():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Enter a number: ").strip()
        attempts += 1

        is_valid, error_message = is_valid_guess(guess)
        if not is_valid:
            print(f"Invalid guess: {error_message}")
            continue

        bulls, cows = evaluate_guess(secret_number, guess)
        if bulls == 4:
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(f"Time taken: {duration} seconds.")
            if attempts <= 5:
                print("That's amazing!")
            elif attempts <= 10:
                print("That's average.")
            else:
                print("You can do better.")
            break
        else:
            print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
            print("-" * 47)

if __name__ == "__main__":
    main()
