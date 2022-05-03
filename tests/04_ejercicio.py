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

etiqueta_laptos : WebElement =driver.find_element(By.LINK_TEXT,'Laptops & Notebooks')
assert etiqueta_laptos.is_displayed(), 'No se encontro la etiqueta laptop'
etiqueta_laptos.click()

etiqueta_windows : WebElement =driver.find_element(By.PARTIAL_LINK_TEXT,'Windows')
assert etiqueta_windows.is_displayed(), 'No se encontro la etiqueta windows'
etiqueta_windows.click()


mensaje_no_producto :WebElement=driver.find_element(By.XPATH,'//*[@id="content"]/p')
assert mensaje_no_producto.is_displayed(), 'No se muestra mensaje de que no hay producto'

btn_regresar:WebElement= driver.find_element(By.LINK_TEXT,'Continue')
assert btn_regresar.is_displayed(), 'No se encontro boton para regresar'
btn_regresar.click()


driver.quit()