from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def find_element(self, args) -> WebElement:
        return self.browser.find_element(*args)

    def find_elements(self, args) -> WebElement:
        return self.browser.find_elements(*args)
