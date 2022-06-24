from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage

class TestPomProduct(BasePage):
    """elementos de producto"""
    _name=(By.XPATH,"//*[@id='content']//h1")
    _price=(By.XPATH, "//*[@id='content']//li/h2")
    _tax=(By.XPATH, "//li[contains(normalize-space(.), 'Ex Tax:')]")
    _code=(By.XPATH, "//li[contains(normalize-space(.), 'Product Code:')]")
    _availability=(By.XPATH,"//li[contains(normalize-space(.), 'Availability:')]")
    _description=(By.XPATH, "//*[@id='tab-description']/div")
    _add_btn=(By.ID,"button-cart")
    _review=(By.XPATH,"//*[@class='rating']//a[contains(normalize-space(.), 'reviews')]")
    _cart_total = (By.ID, 'cart-total')
    _samsung_uno=(By.LINK_TEXT,"Samsung SyncMaster 941BW")
    _input_search = (By.NAME, 'search')
    _button_search = (By.XPATH, "//div[@id='search']//button")
 
    def __init__(self, driver:WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)
        
    """Producto"""
    def get_description(self):
        return self._get_text(self._description)
    def get_name(self):
        return self._get_text(self._name)
    def get_price(self):
        return self._get_text(self._price)
    def get_product_code(self):
        return self._get_value_from_label(self._code)
    def _get_value_from_label(self, locator: tuple, delimiter: str = ':', value_index: int = -1):
        value = self._get_text(locator)
        return value.split(delimiter)[value_index].lstrip()    
    def click_element(self):
        self._click(self._samsung_uno)        
    def add_to_cart(self):
        self._click(self._add_btn)   
    def get_cart_total(self):
        return self._get_text(self._cart_total)
    def search(self, text: str):
        self._write(self._input_search, text)
        self._click(self._button_search) 