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

etiqueta_laptos : WebElement =driver.find_element(By.XPATH,'/html/body/div[1]/nav/div[2]/ul/li[2]/a')
assert etiqueta_laptos.is_displayed(), 'No se encontro la etiqueta laptop'
etiqueta_laptos.click()

etiqueta_windows : WebElement =driver.find_element(By.XPATH,'/html/body/div[1]/nav/div[2]/ul/li[2]/div/div/ul/li[2]/a')
assert etiqueta_windows.is_displayed(), 'No se encontro la etiqueta windows'
etiqueta_windows.click()


mensaje_no_producto :WebElement=driver.find_element(By.XPATH,'//*[text()="There are no products to list in this category."]')
assert mensaje_no_producto.is_displayed(), 'No se muestra mensaje de que no hay producto'

btn_regresar:WebElement= driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/a')
assert btn_regresar.is_displayed(), 'No se encontro boton para regresar'
btn_regresar.click()
