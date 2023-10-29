from pylenium.driver import Pylenium

from tests.ui.forms.cart_items_area import CartItemsArea


class CartPage:
    __order_summary_field_locator = "[data-testid='summary_title_collapse']"
    __add_to_cart_button_locator = "addtocart_btn"

    def __init__(self, py: Pylenium):
        self.py = py
        self.cart_items_area = CartItemsArea(py)

    def is_opened(self):
        self.py.get(self.__order_summary_field_locator).should().be_visible()


