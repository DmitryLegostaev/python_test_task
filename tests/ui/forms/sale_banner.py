from pylenium.driver import Pylenium


class SaleBanner:
    __shop_and_save_button_locator = "[data-testid='hero_shop_mattress']"

    def __init__(self, py: Pylenium):
        self.py = py

    def click_shop_and_save_button(self):
        self.py.get(self.__shop_and_save_button_locator).click()
