from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
# import selenium


class SeleniumHelper(object):

    def __init__(self):
        self.browser = webdriver.Chrome()
