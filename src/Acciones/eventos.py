
from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

from selenium.webdriver.common.action_chains import ActionChains #para manejar dobleClik
from selenium.webdriver.common.keys import Keys  #para enviar teclas como ENTER, ESC, etc

import time

class Accion:
    def DobleClickByXpath(self, driver, strXpath):
        element = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH,strXpath)))
        action = ActionChains(driver) # Realiza un doble clic en el elemento
        action.double_click(element).perform()

    def DobleClickById(self, driver, Id):
        element = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.ID,Id)))
        action = ActionChains(driver) # Realiza un doble clic en el elemento
        action.double_click(element).perform()
    
    def ScrollToElementByXpath(self, driver, strXpath):
        #funcion que obtiene las coordenadas de un elemento a y de un elemento B para hacer scroll hasta el segundo elemento.
        print("función en desarrollo")

    def SelectItemDropdownById(self, driver, Id, NItem):
        '''este metodo seleciona un elemento del dropdown, donde primer elemento es 1'''
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.ID,Id))).click()
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'//p-dropdownitem['+str(NItem)+']/li'))).click()

    def SelectItemDropdownByXpath(self, driver, strXpath, NItem):
        '''este metodo seleciona un elemento del dropdown, donde primer elemento es 1'''
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,strXpath))).click()
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'//p-dropdownitem['+str(NItem)+']/li'))).click()
    
    def SetDateByXpath(self, driver, strXpath, date):
        '''Este método inserta fecha en un control inputDate donde date es la fecha en Formato DD/MM/AAAA'''
        driver.find_element(By.XPATH, strXpath).send_keys(date)
        driver.find_element(By.XPATH, strXpath).send_keys(Keys.TAB) #para que el control de calendario se oculte

    def setValueCheckboxByXpath(self, driver, strXpath, value):
        '''Marca o desmarca un checkbox, donde value es 1 o 0'''
        #marcado=driver.find_element_by_xpath(strXpath).get_attribute('checked')
        if (value>0):
            driver.find_element(By.XPATH,strXpath).click() #marca o desmarca checkbox

    def ControlModalByXpath(self,driver,XpathBoton,XpathSpninner1,XpathSpninner2,XpathFiltro,value,XpathItem):
        '''Controla las modales, se le pasa por parametro el xpath del botón que lo desencadena, spinners de espera, control del filto, valor a buscar y elemento a seleccionar'''
        #Busca botón lupa que despliega modal
        self.DobleClickByXpath(driver, XpathBoton)
        #espera que desaparezca el spiner de carga
        start_time = time.time()
        WebDriverWait(driver,90).until(EC.invisibility_of_element((By.XPATH,XpathSpninner1)))
        end_time = time.time()
        tiempo_total= end_time- start_time
        print("MODAL ABIERTA:\n*** Desapareció el spinner #1 en: {:.2f} seg.".format(tiempo_total))

            #salir de modal, click en la X
            #WebDriverWait(driver,30,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/p-dynamicdialog/div/div/div[1]/div'))).click()
        #ingresa valor a buscar,:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, XpathFiltro))).send_keys(str(value))
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, XpathFiltro))).send_keys(Keys.RETURN)

        #espera que desaparezca el segundo spiner de carga
        start_time = time.time()
        WebDriverWait(driver,90).until(EC.invisibility_of_element((By.XPATH,XpathSpninner2)))
        end_time = time.time()
        tiempo_total= end_time- start_time
        print("*** Desapareció el spinner #2 en: {:.2f} seg. **MODAL CERRADA**\n".format(tiempo_total))

        #verifica que exista el contenido en el resultado
        #Queda para despues, por ahora solo hace click en el primer elemento que encuentra, si es que hay...
        time.sleep(0.5) #da tiempo a que se cierre la modal
        #Seleccionar primer elemento de la tabla de resultados
        self.DobleClickByXpath(driver, XpathItem)
        time.sleep(1.5)

    def ControlModalSFByXpath(self,driver,XpathBoton,XpathSpninner1,XpathItem):
        '''Controla las modales, se le pasa por parametro el xpath del botón que lo desencadena, spinner de espera y elemento a seleccionar'''
        #Busca botón lupa que despliega modal
        self.DobleClickByXpath(driver, XpathBoton)
        #espera que desaparezca el spiner de carga
        start_time = time.time()
        WebDriverWait(driver,90).until(EC.invisibility_of_element((By.XPATH,XpathSpninner1)))
        end_time = time.time()
        tiempo_total= end_time- start_time
        print("MODAL ABIERTA:\n*** Desapareció el spinner en: {:.2f} seg. **MODAL CERRADA**\n".format(tiempo_total))
        #Queda para despues, por ahora solo hace click en el primer elemento que encuentra, si es que hay...
        time.sleep(0.5)
        #Seleccionar primer elemento de la tabla de resultados
        self.DobleClickByXpath(driver, XpathItem)
        time.sleep(1.5)
