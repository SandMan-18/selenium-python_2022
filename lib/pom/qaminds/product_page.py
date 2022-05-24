from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage

class ProductPage(BasePage):
    
    _name=(By.XPATH,"//*[@id='content']//h1")
    _price=(By.XPATH, "//*[@id='content']//li/h2")
    _tax=(By.XPATH, "//li[contains(normalize-space(.), 'Ex Tax:')]")
    _code=(By.XPATH, "//li[contains(normalize-space(.), 'Product Code:')]")
    _availability=(By.XPATH,"//li[contains(normalize-space(.), 'Availability:')]")
    _description=(By.XPATH, "//*[@id='tab-description']/div")
    _add_btn=(By.ID,"button-cart")
    _review=(By.XPATH,"//*[@class='rating']//a[contains(normalize-space(.), 'reviews')]")
    
    
    
    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)
        
    def get_name(self):
        return self._get_text(self._name)
        
    def get_price(self):
        return self._get_text(self._price)
    
    def get_ex_tax(self):
        return self._get_value_from_label(self._tax)
        
    def get_product_code(self):
        return self._get_value_from_label(self._code)
        
    def get_availability(self):
        return self._get_value_from_label(self._availability)
        
    def get_description(self):
        return self._get_text(self._description)
    
    def add_to_cart(self):
        self._click(self._add_btn)        
    
    def get_total_reviews(self):
        return self._get_value_from_label(self._review, delimiter=None, value_index=0)
    
    def _get_value_from_label(self, locator: tuple, delimiter: str = ':', value_index: int = -1):
        value = self._get_text(locator)
        return value.split(delimiter)[value_index].lstrip()
