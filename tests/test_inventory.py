import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_inventory():
    driver=webdriver.Chrome()
    
    try: 
        # vuelvo a copiar el login porque se vuelve a repetir
        driver.get("https://www.saucedemo.com/")

        user= driver.find_element(By.ID,"user-name")
        password=driver.find_element(By.ID,"password")
        login_button=driver.find_element(By.ID,"login-button")

        user.send_keys("standard_user")
        password.send_keys("secret_sauce")

        login_button.click()

        # verificar que el titulo esta correcto
        assert driver.title == "Swag Labs"

        wait = WebDriverWait(driver, 10)
    
        #Selecciono a todos los elem de la misma clase
        products = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

        ##print(products)
        print(f"cantidad de elementos:{len(products)}")
        #verificación de existencia de productos
        assert len(products)>0

        first_product=products[0]

        #accedo al nombre prod
        product_name=first_product.find_element(By.CLASS_NAME,"inventory_item_name").text

        #accedo al precio del producto
        product_price=first_product.find_element(By.CLASS_NAME,"inventory_item_price").text

        #validar
        assert product_name == "Sauce Labs Backpack"
        assert product_price == "$29.99"

        #verificar menu burger
        menu=driver.find_element(By.ID,"react-burger-menu-btn")

        #validar si esta visible el elemento
        assert menu.is_displayed()

        #verificar filtro
        filtro=driver.find_element(By.CLASS_NAME,"product_sort_container")

        assert filtro.is_displayed()

    finally:
        driver.quit()
