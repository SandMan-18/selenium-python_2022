from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage

class TestPomRChecktout(BasePage):
    
    """Checkout"""
    _product_home=(By.LINK_TEXT,'MacBook')
    _checkout=(By.LINK_TEXT,'Checkout')
    _btn_account=(By.ID,'button-account')
    _add_btn=(By.ID,"button-cart")
    _user_box=(By.ID, 'input-email')
    _pass_box=(By.ID, 'input-password')
    
    def __init__(self, driver:WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)
        
    """Checkout"""
    def get_checkout_home(self):
        self._click(self._product_home)
        self._click(self._add_btn)
        self._click(self._checkout)
    def get_checkout_account(self):
        self.get_checkout_home()
        self._click(self._btn_account)
    def get_login_user(self):
            return self._get_element(self._user_box)
    def get_login_pass(self):
        return self._get_element(self._pass_box)