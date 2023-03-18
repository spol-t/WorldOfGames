import requests
import random
from py_currency_converter import convert


def get_money_interval(difficulty, dollars):
    ils = convert(amount=dollars, to=['ILS'])
    interval = (ils - 5 - difficulty, ils + 5 - difficulty)
    return interval


def get_guess_from_user():
    guess = float(input('Enter your guess: '))
    return guess


def play(difficulty):
    dollars = random.randint(1, 100)
    interval = get_money_interval(difficulty, dollars)
    print(f'You have ${dollars}, guess how much is it in Israeli Sheqel')
    guess = get_guess_from_user()
    if interval[0] < guess < interval[1]:
        return True
    else:
        return False
