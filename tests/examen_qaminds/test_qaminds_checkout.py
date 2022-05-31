from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.examen_final.test_page import TestPage

class TestCheckoutPage:
    
    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.checkout_page=TestPage(self.driver)
        
    def test_login_checkout(self):
        self.checkout_page.get_checkout_home()
        self.checkout_page.get_login_user()
        self.checkout_page.get_login_pass()
    def test_btn_checkout(self):
        self.checkout_page.get_checkout_account()
    
    
        
    def teardown_method(self):
        if self.driver:
            self.driver.quit()    