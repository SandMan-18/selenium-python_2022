import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

chrome_driver_path='./drivers/chromedriver'
gecko_driver_path='./drivers/geckodriver'

url='https://laboratorio.qaminds.com/'
service =Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
driver.get(url)
time.sleep(3)

etiqueta_tablet : WebElement =driver.find_element(By.LINK_TEXT,'Tablets')
assert etiqueta_tablet.is_displayed(), 'No se encontro'
etiqueta_tablet.click()

tablet_encontrada : WebElement =driver.find_element(By.LINK_TEXT,'Samsung Galaxy Tab 10.1')
assert tablet_encontrada.is_displayed(), 'No se encontro tableta'
tablet_encontrada.click()

precio_tablet:WebElement=driver.find_element(By.XPATH,'//h2[text()="$241.99"]')
assert precio_tablet.is_displayed(),'Precio de tablet no es igual'
assert precio_tablet.text=="$241.99"

button_card:WebElement=driver.find_element(By.XPATH,'//button[@data-original-title="Add to Wish List"]')
assert button_card.is_displayed(), 'No se agrego al carrito'
button_card.click()

button_add :WebElement=driver.find_element(By.ID,'button-cart') 
assert button_add.is_displayed(), 'No encontro boton'
button_add.click()




driver.quit()