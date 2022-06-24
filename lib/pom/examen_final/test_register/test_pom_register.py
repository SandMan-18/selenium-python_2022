from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage

class TestPomRegister(BasePage):
    """Elementos de search"""
    _input_search = (By.NAME, 'search')
    _button_search = (By.XPATH, "//div[@id='search']//button")
    _samsung_uno=(By.LINK_TEXT,"Samsung SyncMaster 941BW")
    _samsung_dos=(By.LINK_TEXT,"Samsung Galaxy Tab 10.1")
    _alert_windows=(By.XPATH,'//p[text()="There is no product that matches the search criteria."]')
    _register=(By.LINK_TEXT,'Register')
    _first_name=(By.ID, 'input-firstname')
    _last_name=(By.ID, 'input-lastname')
    _telephone=(By.ID, 'input-telephone')
    _password_confirm=(By.ID, 'input-confirm')
    _btn_register=(By.XPATH, "//*[@value='Continue']")
    _user_box=(By.ID, 'input-email')
    _myaccount=(By.LINK_TEXT,'My Account')
    _pass_box=(By.ID, 'input-password')   
    _alert=(By.CSS_SELECTOR, '.alert-danger')
    
    def __init__(self, driver:WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)
        
    """Register"""
    def get_register(self):
        self._click(self._myaccount)
        self._click(self._register)
         
    def get_elements(self):
        elements_loc=[self._first_name,self._last_name,self._user_box,self._telephone,self._pass_box,self._password_confirm,self._btn_register]
        for element in elements_loc:
            self._get_element(element)
    
    def alert_password(self, user:str, password:str):
        self._write(self._pass_box, user)
        self._write(self._password_confirm, password)
        self._click(self._btn_register)
        self._get_text(self._alert)