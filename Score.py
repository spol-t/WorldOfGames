from os.path import isfile
from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    score = 0
    points_of_winning = (difficulty * 3) + 5
    if isfile(SCORES_FILE_NAME):
        f = open(SCORES_FILE_NAME, "r")
        score = int(f.read())
        score += points_of_winning
        f.close()
    else:
        score += points_of_winning

    f = open(SCORES_FILE_NAME, "w")
    f.write(str(score))
    f.close()

