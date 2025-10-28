from selene.support.shared import browser


class MainPage():
    def __init__(self):
        self.signin_button = browser.element('.d-none.d-lg-inline-flex')

    def open(self):
        browser.open('/')

    def click_signin(self):
        self.signin_button.click()