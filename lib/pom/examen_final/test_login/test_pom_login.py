from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage

class TestPomLogin(BasePage):
    """Elementos de login"""
    _myaccount=(By.LINK_TEXT,'My Account')
    _login=(By.LINK_TEXT,'Login')
    _user_box=(By.ID, 'input-email')
    _pass_box=(By.ID, 'input-password')
    _btn_login=(By.XPATH, '//*[@value="Login"]')    
    _alert=(By.CSS_SELECTOR, '.alert-danger')
    
    def __init__(self, driver:WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)
          
    def get_login(self):
        self._click(self._myaccount)
        self._click(self._login)
    def get_login_user(self):
        return self._get_element(self._user_box)
    def get_login_pass(self):
        return self._get_element(self._pass_box)
    def is_login_warn_displayed(self, user:str, password:str):
        self._write(self._user_box, user)
        self._write(self._pass_box, password)
        self._click(self._btn_login)
        return self._get_element(self._alert).is_displayed()
    def select_menu(self, menu:str):
        loc = (By.PARTIAL_LINK_TEXT, menu)
        self._click(loc)