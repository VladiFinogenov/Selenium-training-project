from src.page.product_page import ProductPage
from src.page.login_page import LoginPage
from src.page.main_page import MainPage
from src.utils.captcha import solve_quiz_and_get_code


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_add_product_to_basket1(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_cart()
    solve_quiz_and_get_code(page.browser)


def test_guest_can_add_product_to_basket2(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_cart()
    solve_quiz_and_get_code(page.browser)