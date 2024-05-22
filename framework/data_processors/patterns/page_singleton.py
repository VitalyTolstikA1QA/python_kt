from playwright.sync_api import Page


class PageSingleton:
    _instance = None

    @classmethod
    def get_instance(cls, page: Page = None) -> Page:
        if cls._instance is None and page is not None:
            cls._instance = page
        return cls._instance

    @classmethod
    def clear_instance(cls):
        cls._instance = None
