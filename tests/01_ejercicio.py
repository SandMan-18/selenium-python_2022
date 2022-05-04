from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

chrome_driver_path='./drivers/chromedriver'
gecko_driver_path='./drivers/geckodriver'

url='https://laboratorio.qaminds.com/'
service =Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

driver.implicitly_wait(10)

driver.get(url)

input_search : WebElement =driver.find_element(By.NAME,'search')
assert input_search.is_displayed(), 'No se encontro'
input_search.clear()
input_search.send_keys('iphone')
busqueda: WebElement=driver.find_element(By.XPATH,'//*[@id="search"]//button')
busqueda.click()
image:WebElement=driver.find_element(By.XPATH,'//img[@title="iPhone"]')
assert image.is_displayed(), 'No se encontro imagen'

driver.quit()