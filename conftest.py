import pytest
from selene import browser
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope='session')
def browser_settings():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1000
    browser.config.window_width = 1800
