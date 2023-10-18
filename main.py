from login import Sesion
from contratoReg import Contrato

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService #para no estar descargando el chromedriver
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == "__main__":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window() #creo que es obvio lo que hace
    driver.get("https://previexappdev.azurewebsites.net")

Sesion().iniciar(driver) #inicia los procesos comentados de abajo
Contrato().Registrar(driver)

'''sesion=Sesion()
sesion.iniciar(driver)
contrato=Contrato()
contrato.Registrar(driver)'''

input("***Presiona ENTER para cerrar el navegador...") #para evitar que se cierre al culminar el script

driver.quit()




