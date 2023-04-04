import random
import time
import Utils


def generate_sequence(difficulty):
    numbers_list = []
    for i in range(0, difficulty):
        numbers_list.append(random.randint(1, 101))
    return numbers_list


def get_list_from_user(difficulty):
    numbers_list = []
    for i in range(0, difficulty):
        numbers_list.append(int(input(f'Enter a the {i+1}th number: ')))
    return numbers_list


def is_list_equal(list1, list2):
    if list1 == list2:
        return True
    else:
        return False


def play(difficulty):
    numbers_list = generate_sequence(difficulty)
    print(numbers_list)
    time.sleep(0.7)
    Utils.screen_cleaner()
    user_list = get_list_from_user(difficulty)
    return is_list_equal(numbers_list, user_list)

