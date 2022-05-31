from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.examen_final.test_page import TestPage

class TestSearchPage:
    
    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.test_page=TestPage(self.driver)
    def test_search_windows(self):
        self.test_page.search('Windows')
        self.test_page.search_windows()
        
    def test_search_samsung(self):
        self.test_page.search('Samsung')
        self.test_page.get_samsung()
        
    
        
    def teardown_method(self):
        if self.driver:
            self.driver.quit()    