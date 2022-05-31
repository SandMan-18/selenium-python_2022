from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.examen_final.test_page import TestPage

class TestLoginPage:
    
    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.login_page=TestPage(self.driver)
    
    def test_login_box(self):
        self.login_page.get_login()
        self.login_page.get_login_user()
        self.login_page.get_login_pass()
        
    def test_invalid_login(self):
        self.login_page.get_login()
        assert self.login_page.is_login_warn_displayed('user','password'), "Warn shoul be displayed"
    
    def test_opcion_menu(self):
        self.login_page.get_login()
        for menu in ['Login','Register','Forgotten Password']:
            self.login_page.select_menu(menu)
        
        
    def teardown_method(self):
        if self.driver:
            self.driver.quit()    