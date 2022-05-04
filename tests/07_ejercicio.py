from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# Open Web Page
driver.get(url)


wait = WebDriverWait(driver, 10)

locator=(By.ID,'at-cv-lightbox-close')
cerrar_popup=wait.until(EC.visibility_of_element_located(locator))
cerrar_popup:WebElement=wait.until(EC.element_to_be_clickable(locator))

assert cerrar_popup.is_enabled(), 'cerrar popup no esta habilitado'
cerrar_popup.click()

driver.quit()
