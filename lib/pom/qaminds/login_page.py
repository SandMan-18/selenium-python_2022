from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage


class LoginPage(BasePage):
    _user_box=(By.ID, 'input-email')
    _pass_box=(By.ID, 'input-password')
    _btn_login=(By.XPATH, '//*[@value="Login"]')
    _forggotten=(By.LINK_TEXT,'Forgotten Password')
    _continue=(By.LINK_TEXT,'Continue')
    _alert=(By.CSS_SELECTOR, '.alert-danger')
    
    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)
        
    def login(self, user:str, password:str):
        self._write(self._user_box, user)
        self._write(self._pass_box, password)
        self._click(self._btn_login)
        
    def forgotten_password(self):
        self._click(self._forggotten)
        
    def select_menu(self, menu:str):
        loc = (By.PARTIAL_LINK_TEXT, menu)
        self._click(loc)
        
    def continue_as_new_customer(self):
        self._click(self._continue)
        
    def is_login_warn_displayed(self):
        return self._get_element(self._alert).is_displayed()
        
        