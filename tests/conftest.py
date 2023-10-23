
from selene import browser
import pytest


@pytest.fixture( scope='function', autouse=True)
def browser_set():
    browser.config.window_width = 920
    browser.config.window_height = 1280

    yield

    browser.quit()
