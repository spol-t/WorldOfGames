import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

webdriver_service = Service('~/Downloads/chromedriver')
my_driver = webdriver.Chrome(service=webdriver_service)


def test_scores_service(url='http://127.0.0.1:5001'):
    my_driver.get(url)
    score_element = my_driver.find_element(By.ID, 'score')
    score_string = score_element.text
    score = int(score_string.split()[-1])
    if 0 < score < 1000:
        return True
    else:
        return False


def main():
    results = test_scores_service()
    my_driver.quit()
    if results:
        return sys.exit(0)
    else:
        return sys.exit(1)


main()