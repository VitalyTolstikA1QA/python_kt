import pytest
from framework.utils.browser_factory import init_browser
from framework.utils.settins_utils import settings


@pytest.fixture()
def browser():
    browser = init_browser()
    browser.maximize_window()
    browser.implicitly_wait(settings.implicitly_wait)
    yield browser
    browser.quit()
