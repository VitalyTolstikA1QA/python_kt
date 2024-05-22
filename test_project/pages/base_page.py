from framework.data_processors.patterns.page_singleton import PageSingleton
from framework.utils.config_utils import config


class BasePage:
    def __init__(self):
        self.page = PageSingleton.get_instance()
        self.width = 1820
        self.height = 880

    def open(self, url=config.base_ui_url):
        self.page.set_viewport_size({"width": self.width, "height": self.height})
        self.page.goto(url)
