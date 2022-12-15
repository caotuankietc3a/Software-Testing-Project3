from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Utils:
    # Static variable
    # driver = webdriver.Chrome(
    #     service=Service(ChromeDriverManager().install()))
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()))

    def __init__(self):
        pass
