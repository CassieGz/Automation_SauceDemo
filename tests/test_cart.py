import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart():
    driver=webdriver.Chrome()
    try: 
        #login
        driver.get("https://www.saucedemo.com/")

        user= driver.find_element(By.ID,"user-name")
        password=driver.find_element(By.ID,"password")
        login_button=driver.find_element(By.ID,"login-button")

        user.send_keys("standard_user")
        password.send_keys("secret_sauce")

        login_button.click()

        wait = WebDriverWait(driver, 10)

         # Agregar producto mochila al carrito
         # Busco el elemento
        add_button=wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        

        #Hago click
        add_button.click()
    
        #validar que cambio de estado 'add to cart' a remove
        remove_button = wait.until(
                EC.visibility_of_element_located((By.ID, "remove-sauce-labs-backpack"))
            )
        assert remove_button.text == "Remove"
    
        # Verificar si contador subió a 1
        # Swag Labs genera esta clase únicamente cuando hay productos dentro
        contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert contador.text == "1"

        # Hacer clic en el carrito para navegar a él
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
        # Validación que estoy en la URL del carrito
        assert "cart.html" in driver.current_url
    
        #pausa
        time.sleep(2)

    finally:
        driver.quit()