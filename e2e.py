import sys

from selenium import webdriver
from selenium.webdriver.common.by import By

my_driver = webdriver.Chrome('~/Downloads/chromedriver')


def test_scores_service(url='http://localhost:5000'):
    my_driver.get(url)
    score_string = str(my_driver.find_element(By.ID, 'score'))
    score = int(score_string.split()[-1])
    if 0 < score < 1000:
        return True
    else:
        return False


def main():
    if test_scores_service():
        return sys.exit(0)
    else:
        return sys.exit(-1)





