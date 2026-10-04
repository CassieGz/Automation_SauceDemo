import pytest
from selenium import webdriver
#para importar elem por selectores
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_exitoso():
#inicio el navegador en la var driver
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver,10)

    #prueba
    try: 
        driver.get("https://www.saucedemo.com/")

        #busco los elem -- defino variables y ejecuto instrucciones(acciones)
        #user= driver.find_element(By.ID,"user-name")
        user=wait.until(EC.presence_of_element_located((By.ID,"user-name")))
        
        #password=driver.find_element(By.ID,"password")
        password=wait.until(EC.presence_of_element_located((By.ID,"password")))
        
        #login_button=driver.find_element(By.ID,"login-button")
        login_button=wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

        #le envio las credenciasle a usuario
        user.send_keys("standard_user")
        password.send_keys("secret_sauce")

        # hago click
        login_button.click()

        #validaciones que existe inventory
        assert "/inventory.html" in driver.current_url

        #validar que existe swag labs - estaba en el elem logo
        #Validación texto
        logo = driver.find_element(By.CLASS_NAME,"app_logo")

        assert logo.text == "Swag Labs"

        #Validar data
        titulo=driver.find_element(By.CSS_SELECTOR,'[data-test="title"]')
        assert titulo.text == "Products"
    
    finally:
        driver.quit()
