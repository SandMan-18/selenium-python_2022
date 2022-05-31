from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage

class TestPage(BasePage):
    """Elementos de home"""
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
    """Elementos de login"""
    _myaccount=(By.LINK_TEXT,'My Account')
    _login=(By.LINK_TEXT,'Login')
    _user_box=(By.ID, 'input-email')
    _pass_box=(By.ID, 'input-password')
    _btn_login=(By.XPATH, '//*[@value="Login"]')    
    _alert=(By.CSS_SELECTOR, '.alert-danger')
    """Elementos de search"""
    _input_search = (By.NAME, 'search')
    _button_search = (By.XPATH, "//div[@id='search']//button")
    _samsung_uno=(By.LINK_TEXT,"Samsung SyncMaster 941BW")
    _samsung_dos=(By.LINK_TEXT,"Samsung Galaxy Tab 10.1")
    _alert_windows=(By.XPATH,'//p[text()="There is no product that matches the search criteria."]')
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
    """Elementos de login"""
    _register=(By.LINK_TEXT,'Register')
    _first_name=(By.ID, 'input-firstname')
    _last_name=(By.ID, 'input-lastname')
    _telephone=(By.ID, 'input-telephone')
    _password_confirm=(By.ID, 'input-confirm')
    _btn_register=(By.XPATH, "//*[@value='Continue']")
    
    """Checkout"""
    _product_home=(By.LINK_TEXT,'MacBook')
    _checkout=(By.LINK_TEXT,'Checkout')
    _btn_account=(By.ID,'button-account')
    
    
    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)
  
    """Home"""   
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
         
     
    """Login"""    
    def get_login(self):
        self._click(self._myaccount)
        self._click(self._login)
    def get_login_user(self):
        return self._get_element(self._user_box)
    def get_login_pass(self):
        return self._get_element(self._pass_box)
    def is_login_warn_displayed(self, user:str, password:str):
        self._write(self._user_box, user)
        self._write(self._pass_box, password)
        self._click(self._btn_login)
        return self._get_element(self._alert).is_displayed()
    def select_menu(self, menu:str):
        loc = (By.PARTIAL_LINK_TEXT, menu)
        self._click(loc)
        
    """Search"""    
    def search(self, text: str):
        self._write(self._input_search, text)
        self._click(self._button_search)
    def search_windows(self):
        self._get_text(self._alert_windows)
    
    def get_samsung(self):
        elements_samsung=[self._samsung_uno,self._samsung_dos]
        for element in elements_samsung:
            self._get_element(element)    
        
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
    
    """Register"""
    def get_register(self):
        self._click(self._myaccount)
        self._click(self._register)
         
    def get_elements(self):
        elements_loc=[self._first_name,self._last_name,self._user_box,self._telephone,self._pass_box,self._password_confirm,self._btn_register]
        for element in elements_loc:
            self._get_element(element)
        
    
    def alert_password(self, user:str, password:str):
        self._write(self._pass_box, user)
        self._write(self._password_confirm, password)
        self._click(self._btn_register)
        self._get_text(self._alert)
        
    """Checkout"""
    def get_checkout_home(self):
        self._click(self._product_home)
        self._click(self._add_btn)
        self._click(self._checkout)
    def get_checkout_account(self):
        self.get_checkout_home()
        self._click(self._btn_account)
       
    
    
    