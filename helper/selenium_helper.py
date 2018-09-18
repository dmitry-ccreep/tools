from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import config
import os


class SeleniumHelper(object):

    def __init__(self):
        os.environ["PATH"] += os.pathsep + config.DRIVER_PATH
        self.browser = webdriver.Chrome()
        self.browser.get('http://yandex.ru')
        assert 'Django' in self.browser.title