from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from lib.factory.factory_driver import get_driver


driver= get_driver("Firefox")

driver.implicitly_wait(10)

driver.get("https://laboratorio.qaminds.com/")

input_search : WebElement =driver.find_element(By.NAME,'search')
assert input_search.is_displayed(), 'No se encontro'
input_search.clear()
input_search.send_keys('iphone')
busqueda: WebElement=driver.find_element(By.XPATH,'//*[@id="search"]//button')
busqueda.click()
image:WebElement=driver.find_element(By.XPATH,'//img[@title="iPhone"]')
assert image.is_displayed(), 'No se encontro imagen'

driver.quit()