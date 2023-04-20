import os
from os.path import isfile, exists
from Utils import SCORES_FILE_NAME


def is_file_empty(file_path):
    return exists(file_path) and os.stat(file_path).st_size == 0


def get_score():
    if is_file_empty(SCORES_FILE_NAME):
        score = 0
    else:
        f = open(SCORES_FILE_NAME, 'r')
        score = int(f.read())
        f.close()
    return score


def add_score(difficulty):
    score = 0
    points_of_winning = (difficulty * 3) + 5
    if isfile(SCORES_FILE_NAME):
        score = get_score()
        score += points_of_winning
    else:
        score += points_of_winning

    f = open(SCORES_FILE_NAME, "w")
    f.write(str(score))
    f.close()
