import time
from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

from selenium.webdriver.common.action_chains import ActionChains #para manejar dobleClik

class Contrato:
    def Registrar(self, driver):
        #para abrir el panel principal...
        element = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="header"]/div/i')))
        action = ActionChains(driver) # Realiza un doble clic en el elemento
        action.double_click(element).perform()

        time.sleep(2) #da tiempo a que se despliegue el menú principal

        #Busca el menú contrato
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-side-menu/div/ul/app-menu-item[1]/a/i[2]'))).click()
        #Busca el menú Empresarial
        WebDriverWait(driver,90,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-side-menu/div/ul/app-menu-item[1]/div/div/app-menu-item[1]/a'))).click()
            #Busca el menú Activaión
            #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-side-menu/div/ul/app-menu-item[1]/div/div/app-menu-item[1]/div/div/app-menu-item[1]'))).click()
        #Busca el menú Gestión
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-side-menu/div/ul/app-menu-item[1]/div/div/app-menu-item[1]/div/div/app-menu-item[2]'))).click()
        #Busca botón "CREAR"
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-contrato-empresarial-index/p-panel/div/div[1]/div/div/button[2]'))).click()
        #YA EN NUEVA PANTALLA: Busca botón lupa de "Ciudad"
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[2]/p-tabpanel/div/app-contrato-empresarial-info-edit/form/p-panel[1]/div/div[2]/div/div/div/app-dropdown/div/p-dropdown/div/div[2]')))
        action = ActionChains(driver) # Realiza un doble clic en el elemento
        action.double_click(element).perform()

