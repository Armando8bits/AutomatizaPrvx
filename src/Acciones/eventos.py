
from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

from selenium.webdriver.common.action_chains import ActionChains #para manejar dobleClik
from selenium.webdriver.common.keys import Keys  #para enviar teclas como ENTER, ESC, etc

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

    def SelectItemDropdownById(self, driver, Id, NMes):
        '''este metodo seleciona un mes en el dropdown mes de contrato
        donde NMes (numero de mes) es un numero del 1 al 12'''
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.ID,Id))).click()
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'//p-dropdownitem['+str(NMes)+']/li'))).click()
    
    def SetDateByXpath(self, driver, strXpath, date):
        '''Este método inserta fecha en un control inputDate donde date es la fecha en Formato DD/MM/AAAA'''
        driver.find_element(By.XPATH, strXpath).send_keys(date)
        driver.find_element(By.XPATH, strXpath).send_keys(Keys.TAB) #para que el control de calendario se oculte

    def setValueCheckboxByXpath(self, driver, strXpath, value):
        '''Marca o desmarca un checkbox, donde value es 1 o 0'''
        marcado=driver.find_element_by_xpath(strXpath).get_attribute('checked')
        #if ():