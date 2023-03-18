import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        guess = int(input(f"Guess a number between 1 and {difficulty}: "))
        if guess in range(1, difficulty + 1):
            break
        else:
            print("The number you guessed is not in range")

    return guess


def compare_results(guess, secret_number):
    if guess == secret_number:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(guess, secret_number)

