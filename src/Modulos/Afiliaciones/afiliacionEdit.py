import time
from ...Acciones import eventos
#para efectuar los doble cliks y otros
Evento=eventos.Accion()
from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

class Afiliacion:
    def Editar(self, driver):
        #para abrir el panel principal...
        Evento.DobleClickByXpath(driver, '//*[@id="header"]/div/i')
        time.sleep(2) #da tiempo a que se despliegue el menú principal
        #Busca el menú contrato
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'//ul/app-menu-item[2]/a'))).click()
        time.sleep(0.5)
        #Busca el menú Empresarial
        WebDriverWait(driver,90,2).until(EC.element_to_be_clickable((By.XPATH,'//ul/app-menu-item[2]/div/div/app-menu-item/div/a'))).click()
        #Busca el input "Numero de contrato" y ahreha el numero de contrato
        WebDriverWait(driver,90,2).until(EC.element_to_be_clickable((By.XPATH,'//input'))).send_keys(303)
        #click en botñon BUSCAR y seleccionar contrato
        Evento.ControlModalSeleccionByXpath(driver,'//span/i',
                                   '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                   '/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/app-spinner',
                                   '//td[8]/button/span')
        time.sleep(0.5)
        #da click en editar
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-afiliacion-empresarial-index/p-panel/div/div[2]/div/div[2]/app-afiliacion-empresarial-list/p-panel/div/div[2]/div/div/div/p-table/div/div/table/tbody/tr[1]/td[8]/div/button[3]/span'))).click()
        Evento.ManageSpinnerByXpath(driver, '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner')
        time.sleep(1)
        #---------YA EN NUEVA PANTALLA:
        print(">> EDITANDO AFILIACION EMPRESARIAL")
        #se cambia a pestaña ADICIONALES
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-afiliacion-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[1]/div/ul/li[3]/a/span'))).click()
        #oprime botón "+"
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-afiliacion-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[2]/p-tabpanel[3]/div/app-afiliacion-empresarial-adicionales-list/p-panel/div/div[2]/div/div[1]/div[1]/button[1]'))).click()
        #



