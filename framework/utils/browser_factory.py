from framework.utils.settins_utils import settings
from selenium import webdriver


def init_browser():
    if settings.browser == 'chrome':
        return webdriver.Chrome()
    else:
        return webdriver.Firefox()
