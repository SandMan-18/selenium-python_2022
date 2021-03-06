from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage


class HomePage(BasePage):
    _logo = (By.ID, 'logo')
    _input_search = (By.NAME, 'search')
    _button_search = (By.XPATH, "//div[@id='search']//button")
    _cart_total = (By.ID, 'cart-total')
    _currency=(By.XPATH,'//*[@id="form-currency"]//strong')
    _currency_drop=(By.XPATH,'//*[@id="form-currency"]//button[@data-toggle]')

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def is_logo_visible(self) -> bool:
        return self._get_element(self._logo).is_displayed()

    def search(self, text: str):
        self._write(self._input_search, text)
        self._click(self._button_search)

    def select_menu(self, menu_name: str):
        loc = (By.PARTIAL_LINK_TEXT, menu_name)
        self._click(loc)

    def select_sub_menu(self, main_menu_name: str, sub_menu_name: str):
        self.select_menu(main_menu_name)
        self.select_menu(sub_menu_name)

    def get_cart_total(self) -> str:
        return self._get_text(self._cart_total)

    def get_currency(self):
        return self._get_text(self._currency)


    def set_currency(self, name: str):
        self._click(self._currency_drop)
        loc = (By.XPATH, f'//*[@id="form-currency"]//button[@name="{name}"]')
        self._click(loc)

    def select_product(self, name: str):
        loc = (By.PARTIAL_LINK_TEXT, name)
        self._click(loc)