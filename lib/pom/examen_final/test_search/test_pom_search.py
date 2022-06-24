from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage

class TestPomSearch(BasePage):
    _input_search = (By.NAME, 'search')
    _button_search = (By.XPATH, "//div[@id='search']//button")
    _samsung_uno=(By.LINK_TEXT,"Samsung SyncMaster 941BW")
    _samsung_dos=(By.LINK_TEXT,"Samsung Galaxy Tab 10.1")
    _alert_windows=(By.XPATH,'//p[text()="There is no product that matches the search criteria."]')
    
    def __init__(self, driver:WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)
        
    def search(self, text: str):
        self._write(self._input_search, text)
        self._click(self._button_search)
    def search_windows(self):
        self._get_text(self._alert_windows)
    
    def get_samsung(self):
        elements_samsung=[self._samsung_uno,self._samsung_dos]
        for element in elements_samsung:
            self._get_element(element)   