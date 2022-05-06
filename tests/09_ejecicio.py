from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# Open Web Page
driver.get(url)

wait = WebDriverWait(driver, 25)


locator=(By.ID,'cricle-btn')
btn_descarga:WebElement=wait.until(EC.element_to_be_clickable(locator))
assert btn_descarga.is_displayed, 'El boton no esta disponible'
btn_descarga.click()

locator_label=(By.CSS_SELECTOR,'.percenttext')
assert wait.until(EC.text_to_be_present_in_element(locator_label,"100%")), "100 no se muestra en pantalla"

driver.quit()