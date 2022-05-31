from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.examen_final.test_page import TestPage

class TestProductPage:
    
    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.test_page=TestPage(self.driver)
    
    def test_info_samsung(self):
        self.search_element()
        description = """Imagine the advantages of going big without slowing down. The big 19" 941BW monitor combines wide aspect ratio with fast pixel response time, for bigger images, more room to work and crisp motion. In addition, the exclusive MagicBright 2, MagicColor and MagicTune technologies help deliver the ideal image in every situation, while sleek, narrow bezels and adjustable stands deliver style just the way you want it. With the Samsung 941BW widescreen analog/digital LCD monitor, it's not hard to imagine."""
        assert self.test_page.get_description()==description
        assert self.test_page.get_name()=='Samsung SyncMaster 941BW'
        assert self.test_page.get_price()== '$242.00'
        assert self.test_page.get_product_code()== 'Product 6'
        
    def test_add_to_cart(self):
        self.search_element()
        self.test_page.add_to_cart()   
    
    def test_cart_total(self):
        self.search_element()
        self.test_page.add_to_cart()
        total = self.test_page.get_cart_total()
        assert "1 item(s) - $242.00" == total     
        
    def search_element(self):
        self.test_page.search('Samsung')
        self.test_page.click_element()      
        
    def teardown_method(self):
        if self.driver:
            self.driver.quit()    