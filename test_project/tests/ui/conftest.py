import pytest

from framework.data_processors.patterns.page_singleton import PageSingleton
from playwright.sync_api import Page


@pytest.fixture
def init_page(page: Page):
    yield PageSingleton.get_instance(page)
    PageSingleton.clear_instance()
