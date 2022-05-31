from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.examen_final.test_page import TestPage

class TestHomePage:
    
    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.home_page=TestPage(self.driver)
        
    def test_currency(self):
        assert '$'== self.home_page.get_currency()
        self.home_page.set_currency('EUR')
        assert "€" == self.home_page.get_currency()
        assert self.home_page.currency_product()=='472.33€\nEx Tax: 392.30€'
    def test_windows(self):
        assert self.home_page.windows_home()=='There are no products to list in this category.'
    def test_software(self):
        assert self.home_page.software_home()=='There are no products to list in this category.'    
        self.home_page.btn_continue()
        
    def teardown_method(self):
        if self.driver:
            self.driver.quit()    