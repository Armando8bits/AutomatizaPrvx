import time
from ...Acciones import eventos
#para efectuar los doble cliks y otros
Evento=eventos.Accion()
from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

class Afiliacion:
    def Registrar(self, driver):
        #para abrir el panel principal...
        Evento.DobleClickByXpath(driver, '//*[@id="header"]/div/i')
        time.sleep(2) #da tiempo a que se despliegue el menú principal
        #Busca el menú contrato
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'//ul/app-menu-item[2]/a'))).click()
        #Busca el menú Empresarial
        WebDriverWait(driver,90,2).until(EC.element_to_be_clickable((By.XPATH,'//ul/app-menu-item[2]/div/div/app-menu-item/div/a'))).click()
        #Busca el input "Numero de contrato" y ahreha el numero de contrato
        WebDriverWait(driver,90,2).until(EC.element_to_be_clickable((By.XPATH,'//input'))).send_keys(303)
        #driver.find_element(By.XPATH, "//span/i").click()

        Evento.ControlModalSeleccionByXpath(driver,'//span/i',
                                   '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                   '/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/app-spinner',
                                   '//td[8]/button/span')
        WebDriverWait(driver,90,1).until(EC.element_to_be_clickable((By.XPATH,'//app-afiliacion-empresarial-list/p-panel/div/div/div/div/button/span[2]'))).click()
        Evento.ManageSpinnerByXpath(driver, '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner')
        time.sleep(0.5)
        WebDriverWait(driver,90,1).until(EC.element_to_be_clickable((By.XPATH,"//p-inputmask[@id='secuencialAfiliacion']/input"))).click()
        driver.find_element(By.XPATH, "//p-inputmask[@id='secuencialAfiliacion']/input").send_keys("tyt565656568")
        # Encuentra el input desabilitado
        print(Evento.GetValueInputDisabledById(driver, "secuencialContrato"))



        print(">> REGISTRANDO NUEVA AFILIACION EMPRESARIAL")