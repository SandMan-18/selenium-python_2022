from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage

class TestPomHome(BasePage):
    
    _currency=(By.XPATH,'//*[@id="form-currency"]//strong')
    _currency_drop=(By.XPATH,'//*[@id="form-currency"]//button[@data-toggle]')
    _menu_lap=(By.LINK_TEXT,'Laptops & Notebooks')
    _menu_windows=(By.LINK_TEXT, 'Windows (0)')
    _no_product=(By.XPATH,'//*[@id="content"]/p')
    _menu_software=(By.LINK_TEXT,'Software')
    _btn_continue=(By.LINK_TEXT,'Continue')
    _currency_product=(By.XPATH,'//p[contains(normalize-space(.), "€")]')
    _dolar=(By.XPATH,"//*[@id='form-currency']//strong")
    _euro=(By.XPATH,"//*[@id='form-currency']//strong")

    """Home"""   
    def __init__(self, driver:WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)
    
    def get_currency(self):
        return self._get_text(self._currency)
    def set_currency(self, name: str):
        self._click(self._currency_drop)
        loc = (By.XPATH, f'//*[@id="form-currency"]//button[@name="{name}"]')
        self._click(loc)
    def currency_product(self):   
        return self._get_text(self._currency_product)        
    def windows_home(self):
        self._click(self._menu_lap)
        self._click(self._menu_windows)
        return self._get_text(self._no_product)  
    def software_home(self):
        self._click(self._menu_software)
        return self._get_text(self._no_product)  
    def btn_continue(self):
        self._click(self._btn_continue)      
         

