
from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

from selenium.webdriver.common.action_chains import ActionChains #para manejar dobleClik

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