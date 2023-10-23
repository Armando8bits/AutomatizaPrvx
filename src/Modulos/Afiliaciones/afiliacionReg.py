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
        #click en botón CREAR
        WebDriverWait(driver,90,2).until(EC.element_to_be_clickable((By.XPATH,'//app-afiliacion-empresarial-list/p-panel/div/div/div/div/button/span[2]'))).click()
        Evento.ManageSpinnerByXpath(driver, '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner')
        time.sleep(0.5)
        #---------YA EN NUEVA PANTALLA: establece "Secuencial pre-impreso":
        print(">> REGISTRANDO NUEVA AFILIACION EMPRESARIAL")
        WebDriverWait(driver,90,1).until(EC.element_to_be_clickable((By.XPATH,"//p-inputmask[@id='secuencialAfiliacion']/input"))).click()
        driver.find_element(By.XPATH, "//p-inputmask[@id='secuencialAfiliacion']/input").send_keys("tyt565656570")
        #Establece Fecha afiliación
        Evento.SetDateByXpath(driver,"//span/input","25/02/2023")
        #scroll abajo para que elemento sea visible
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.25)") #*0.25 para que baje menos de lo normal
        time.sleep(1.5) #DA TIEMPO A QUE BAJE LA PAGINA
        #Establece Persona
        Evento.ControlModalByXpath(driver,'//app-dropdown/div/button',
                                   '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                   '/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/app-spinner',
                                   '//th[3]/p-columnfilter/div/p-columnfilterformelement/input',
                                   'PAMELA','//td[3]')
        time.sleep(0.5)
        #scroll abajo para que elemento sea visible
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.6)")
        time.sleep(1.5) #DA TIEMPO A QUE BAJE LA PAGINA
        #Escoge PLAn
        Evento.ControlModalSFByCssSelector(driver,'//p-panel[3]/div/div[2]/div/div/div/app-dropdown/div/button/span',
                                   '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                   '2','3') #.p-element:nth-child(3) > .centrar-datos:nth-child(3)
        #Escoge Alternativa
        Evento.ControlModalSFByCssSelector(driver,'//div[2]/app-dropdown/div/button/span',
                                   '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                   '3','3') #.p-element:nth-child(3) > .centrar-datos:nth-child(3)
        #scroll abajo para que elemento sea visible
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1.5) #DA TIEMPO A QUE BAJE LA PAGINA
        #controla modal de Ejecutivo de AFILIACION
        Evento.ControlModalByXpath(driver,'//p-panel[4]/div/div[2]/div/div/div/app-dropdown/div/button/span',
                                   '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                   '/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/app-spinner',
                                   '//th[3]/p-columnfilter/div/p-columnfilterformelement/input',
                                   "STEFANIE",'//td[3]')
        #Click botón GRABAR
        driver.find_element(By.XPATH, '//form/div[2]/button').click()
        #confirma los cambios
        Evento.ManageSpinnerByXpath(driver, '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner')
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'//app-validate-data-and-get-tariff-dialog/div/button/span'))).click()
        Evento.ManageSpinnerByXpath(driver, '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner')
        #obtiene numero de Afiliacion
        print("Se generó exitosamente Afiliación empresarial: "+str(Evento.GetValueInputDisabledByXpath(driver, '/html/body/app-root/app-content-layout/div/app-afiliacion-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[2]/p-tabpanel[1]/div/app-afiliacion-empresarial-info-edit/form/p-panel[1]/div/div[2]/div/div[2]/div[2]/input')))
        #se cambia a pestaña ADICIONALES
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-afiliacion-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[1]/div/ul/li[3]/a/span'))).click()
        #oprime botón "+"
        WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-afiliacion-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[2]/p-tabpanel[3]/div/app-afiliacion-empresarial-adicionales-list/p-panel/div/div[2]/div/div[1]/div[1]/button[1]'))).click()
        #



        #driver.find_element(By.XPATH , '//img').click()  #sale a pantalla principal


        