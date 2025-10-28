import pytest

from selenium import webdriver
from selene.support.shared import browser


@pytest.fixture(scope="function")
def setup_browser():

    browser.config.base_url = "https://github.com/"

    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--incognito")
    driver_options.page_load_strategy = "eager"
    # driver_options.add_argument("--window-size=1920,1280")
    driver_options.add_argument("--window-size=1280,720")

    browser.config.driver = webdriver.Chrome(options=driver_options)

    yield
    browser.quit()