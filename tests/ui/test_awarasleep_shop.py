import allure

from tests.ui.pages.cart_page import CartPage
from tests.ui.pages.main_page import MainPage
from tests.ui.pages.mattress_page import MattressPage


class TestAwaraSleepShop:
    @allure.title("Add mattress to cart by banner on Main page")
    @allure.description(
        "A test which should open https://qa.awarasleep.com/, click on banner and add mattress to the cart")
    @allure.suite("UI")
    def test_add_mattress_to_cart_by_banner(self, py, retrieve_ui_url_endpoint):
        with allure.step("Open main page"):
            py.visit(retrieve_ui_url_endpoint)
        with allure.step("Check that main page is opened"):
            main_page = MainPage(py)
            main_page.is_opened()
        with allure.step("Click shop and save button"):
            main_page.sale_banner.click_shop_and_save_button()
        with allure.step("Check that mattress page is opened"):
            mattress_page = MattressPage(py)
            mattress_page.is_opened()
        with allure.step("Add mattress to the cart"):
            mattress_page.click_add_to_cart_button()
        with allure.step("Check that mattress is added to the cart"):
            cart_page = CartPage(py)
            cart_page.is_opened()
            cart_page.cart_items_area.contains_single_item("Mattress")
