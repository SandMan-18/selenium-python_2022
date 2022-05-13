from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# Open Web Page
driver.get(url)

wait = WebDriverWait(driver, 10)


locator=(By.ID,'autoclosable-btn-success')
btn_success:WebElement=wait.until(EC.element_to_be_clickable(locator))
assert btn_success.is_displayed, 'El boton no esta disponible'
btn_success.click()

locator_msg=(By.CSS_SELECTOR,'.alert-autocloseable-success')
assert wait.until(EC.visibility_of_element_located(locator_msg))

assert wait.until(EC.invisibility_of_element_located(locator_msg)),'Se sigue mostrando el mensaje'
                  
                  
driver.quit()
