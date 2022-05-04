import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Init Browsers
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = "https://demoqa.com/select-menu"
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# Open Web Page
driver.get(url)

# Test Logic
time.sleep(2)
cars = driver.find_element(By.ID, "cars")
assert cars.is_displayed(), "Cars is not visible"
option_cars=Select(cars)

#Seleccionar varias opciones y verificar que se hayan seleccionado
option_cars.select_by_visible_text("Volvo")
option_cars.select_by_visible_text("Audi")

selected_options: list= [option.text for option in option_cars.all_selected_options]

assert "Volvo" in selected_options, 'Volvo no esta seleccionado'
assert "Audi" in selected_options, 'Audi no esta seleccionado'


# Close browser
driver.quit()