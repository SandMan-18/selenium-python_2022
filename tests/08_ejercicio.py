from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# Open Web Page
driver.get(url)

wait = WebDriverWait(driver, 15)

locator=(By.ID,'downloadButton')
btn_descarga:WebElement=wait.until(EC.element_to_be_clickable(locator))
assert btn_descarga.is_displayed, 'El boton no esta disponible'
btn_descarga.click()

locator_label=(By.XPATH,'//*[@class="progress-label"]')
assert wait.until(EC.text_to_be_present_in_element(locator_label, "Complete!")), 'Complete no se muestra'

locator_btn=(By.XPATH,'//*[@class="ui-dialog-buttonset"]/button')
complete_btn:WebElement=wait.until(EC.element_to_be_clickable(locator_btn))
assert complete_btn.is_enabled, 'El boton close no esta habilitado'

driver.quit()