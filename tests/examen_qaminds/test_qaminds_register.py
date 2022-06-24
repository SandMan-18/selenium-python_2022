from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.examen_final.test_register.test_pom_register import TestPomRegister

class TestRegisterPage:
    
    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.register_page=TestPomRegister(self.driver)
        
    def test_elements_register(self):
        self.register_page.get_register()
        self.register_page.get_elements()
    def test_alert_password(self):
        self.register_page.get_register()
        self.register_page.alert_password('123456','12345678')

    def teardown_method(self):
        if self.driver:
            self.driver.quit()    