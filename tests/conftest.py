import pytest
from selene import browser


@pytest.fixture( scope='function', autouse=True)
def browser_set():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 3

    yield

    browser.quit()