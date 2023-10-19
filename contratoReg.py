import time
from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

from selenium.webdriver.common.action_chains import ActionChains #para manejar dobleClik

from selenium.webdriver.common.keys import Keys  #para enviar teclas como ENTER, ESC, etc

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
        #buscar si se abrió la modal
        #WebDriverWait(driver,90).until(EC.visibility_of((By.XPATH,'/html/body/p-dynamicdialog/div/div'))).click()
        #print("***Apareció la modal...")
        #espera que desaparezca el spiner de carga
        start_time = time.time()
        WebDriverWait(driver,90).until(EC.invisibility_of_element((By.XPATH,'/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner')))
        end_time = time.time()
        tiempo_total= end_time- start_time
        print("***Desapareció el spinner...en: " + str(tiempo_total))

        #salir de modal, click en la X
        #WebDriverWait(driver,30,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/p-dynamicdialog/div/div/div[1]/div'))).click()

        #ingresa nombre de empresa:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/p-panel/div/div[2]/div/p-table/div/div/table/thead/tr[2]/th[3]/p-columnfilter/div/p-columnfilterformelement/input'))).send_keys(str("pichincha"))
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/p-panel/div/div[2]/div/p-table/div/div/table/thead/tr[2]/th[3]/p-columnfilter/div/p-columnfilterformelement/input'))).send_keys(Keys.RETURN)

#espera que desaparezca el spiner de carga
        start_time = time.time()
        WebDriverWait(driver,90).until(EC.invisibility_of_element((By.XPATH,'/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/app-spinner')))
        end_time = time.time()
        tiempo_total= end_time- start_time
        print("***Desapareció el 2do spinner...en: " + str(tiempo_total))

        #verifica que exista el contenido en el resultado
        #Queda para despues, por ahora solo hace click en el primer elemento que encuentra, si es que hay...

        time.sleep(0.5) #da tiempo a que se cierre la modal

        #Seleccionar primer elemento de la tabla de resultados
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/p-panel/div/div[2]/div/p-table/div/div/table/tbody/tr[1]')))
        action = ActionChains(driver) # Realiza un doble clic en el elemento
        action.double_click(element).perform()

        time.sleep(1.5)

        #scroll abajo para que elemento sea visible
        '''WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[2]/p-tabpanel/div/app-contrato-empresarial-info-edit/form/p-panel[1]/div/div[1]/div')))\
                    .send_keys(Keys.PAGE_DOWN)'''
        #driver.execute_script("window.scrollTo(0, 1000);")
        '''element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[2]/p-tabpanel/div/app-contrato-empresarial-info-edit/form/p-panel[3]/div/div[2]/div/div[1]/div[2]/p-dropdown')))
        action = ActionChains(driver) # Realiza un doble clic en el elemento
        action.scroll_to_element(element).click()'''

        #da click en dropdown AÑO
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[2]/p-tabpanel/div/app-contrato-empresarial-info-edit/form/p-panel[3]/div/div[2]/div/div[1]/div[2]/p-dropdown'))).click()

