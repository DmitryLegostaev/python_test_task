from pylenium.driver import Pylenium

from tests.ui.forms.sale_banner import SaleBanner


class MainPage:
    __header_locator = "#header-nav"

    def __init__(self, py: Pylenium):
        self.py = py
        self.sale_banner = SaleBanner(py)

    def is_opened(self):
        self.py.get(self.__header_locator).should().be_visible()
