from pylenium.driver import Pylenium


class MattressPage:
    __mattress_main_option_locator = "[data-testid='awara-latex-hybrid-mattress']"
    __add_to_cart_button_locator = "#addtocart_btn"

    def __init__(self, py: Pylenium):
        self.py = py

    def is_opened(self):
        self.py.get(self.__mattress_main_option_locator).should().be_visible()

    def click_add_to_cart_button(self):
        self.py.get(self.__add_to_cart_button_locator).click()
