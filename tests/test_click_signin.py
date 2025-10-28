import allure
from pages.main_page import MainPage


@allure.story("Клик по кнопке SignIn")
def test_main_page_slogan(setup_browser):
    browser = setup_browser
    main_page = MainPage()

    open_page(main_page)
    click_button(main_page)

@allure.step('Открыть страницу')
def open_page(main_page):
    main_page.open()

@allure.step('Кликнуть по кнопке SignIn')
def click_button(main_page):
    main_page.click_signin()