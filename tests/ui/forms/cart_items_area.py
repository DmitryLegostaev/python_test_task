from pylenium.driver import Pylenium


class CartItemsArea:
    __cart_items_area_locator = "[data-testid='cart_items_area']"

    def __init__(self, py: Pylenium):
        self.py = py

    def get_all_items(self):
        return self.py.get(self.__cart_items_area_locator).children()

    def contains_single_item(self, item_name: str):
        all_items = self.get_all_items()
        all_items.should().have_length(1)
        all_items.first().should().contain_text(item_name)
