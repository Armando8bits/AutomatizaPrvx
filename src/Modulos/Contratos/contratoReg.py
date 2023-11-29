import time
from ...Acciones import eventos
#para efectuar los doble cliks y otros
Evento=eventos.Accion()
from selenium.webdriver.common.by import By #necesario para el de arriba

class Contrato:
    def Registrar(self, driver):
        #para abrir el panel principal...
        Evento.DobleClickByXpath(driver, '/html/body/app-root/app-content-layout/div/app-header/header/div/i')
        #time.sleep(2) #da tiempo a que se despliegue el menú principal

        #Busca el menú contrato
        Evento.WaitClickUntilVisible_Clikeable(driver,'/html/body/app-root/app-content-layout/div/app-side-menu/div/ul/app-menu-item[2]/a')
        #Busca el menú Empresarial
        Evento.WaitClickUntilVisible_Clikeable(driver,'/html/body/app-root/app-content-layout/div/app-side-menu/div/ul/app-menu-item[2]/div/div/app-menu-item[1]/a')
            #Busca el menú Activaión
            #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-side-menu/div/ul/app-menu-item[1]/div/div/app-menu-item[1]/div/div/app-menu-item[1]'))).click()
        #Busca el menú Gestión
        Evento.WaitClickUntilVisible_Clikeable(driver,'/html/body/app-root/app-content-layout/div/app-side-menu/div/ul/app-menu-item[2]/div/div/app-menu-item[1]/div/div/app-menu-item')
        #Busca botón "CREAR"
        Evento.WaitClickUntilVisible_Clikeable(driver,'/html/body/app-root/app-content-layout/div/app-contrato-empresarial-index/p-panel/div/div[1]/div/div/button[2]')
        
        #---------YA EN NUEVA PANTALLA: Busca botón lupa de "Ciudad" para desplegar modal
        print(">> REGISTRANDO NUEVO CONTRATO EMPRESARIAL")
        Evento.ControlModalByXpath(driver,'/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[2]/p-tabpanel/div/app-contrato-empresarial-info-edit/form/p-panel[1]/div/div[2]/div/div/div/app-dropdown/div/p-dropdown/div/div[2]',
                                   '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                   '/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/app-spinner',
                                   '/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/p-panel/div/div[2]/div/p-table/div/div/table/thead/tr[2]/th[3]/p-columnfilter/div/p-columnfilterformelement/input',
                                   'ECUAT','/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/p-panel/div/div[2]/div/p-table/div/div/table/tbody/tr[1]')

        #scroll abajo para que elemento sea visible
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.35)") #*0.25 para que baje menos de lo normal
        time.sleep(1.5) #DA TIEMPO A QUE BAJE LA PAGINA

        #WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[2]/p-tabpanel/div/app-contrato-empresarial-info-edit/form/p-panel[3]/div/div[2]/div/div[1]/div[2]/p-dropdown/div'))).click()
        Evento.SelectItemDropdownById(driver,'pr_id_10_label',2) #selecciona mes
        Evento.SelectItemDropdownById(driver,'pr_id_9_label',2) #selecciona año
        #Evento.SetDateByXpath(driver,"(//input[@type=\'text\'])[10]","25/02/2023") #ingresa fecha

        #establece chec de vigencia inmediata
        Evento.setValueCheckboxByXpath(driver,'//p-checkbox/div/div[2]',0) # 1 activa; 0 no lo toca

        #scroll abajo para que elemento sea visible
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.5)") #0.5 para que baje menos de lo normal
        time.sleep(1.5) #DA TIEMPO A QUE BAJE LA PAGINA

        #el orquestador envia la variable a asignar al ejecutivo si ejecutivo interno está vacio solo selecciona el jefe de venta
        EjecutivoInterno="r"
        if len(EjecutivoInterno)>0: #si viene contenido trabaja con esta modal
            #controla modal de Ejecutivo Interno
            Evento.ControlModalByXpath(driver,'//div[2]/div/div/div/div/app-dropdown/div/button/span',
                                   '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                   '/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/app-spinner',
                                   '//th[4]/p-columnfilter/div/p-columnfilterformelement/input',
                                   EjecutivoInterno,'//td[4]')
        else: #si no, solo configura equipo de venta
            #controla modal de Equipo Venta / Jefe Venta
            Evento.ControlModalSFByCssSelector(driver,'//div[2]/div/app-dropdown/div/button/span',
                                   '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                   '2','5') 
        
        time.sleep(1) #DA TIEMPO

        #controla modal de Ejecutivo Externo
        EjecutivoExterno=False
        if EjecutivoExterno==True:
            Evento.ControlModalByXpath(driver,'//div[2]/app-dropdown/div/button/span',
                                    '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                    '/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/app-spinner',
                                    '//th[3]/p-columnfilter/div/p-columnfilterformelement/input',
                                    't','//td[3]')
        #time.sleep(1) #DA TIEMPO

        #controla modal de Ciudad Contrato
        Evento.ControlModalByXpath(driver,'//p-panel[5]/div/div[2]/div/div/div/div/app-dropdown/div/button/span',
                                   '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                   '/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/app-spinner',
                                   '//th[3]/p-columnfilter/div/p-columnfilterformelement/input',
                                   'g','//td[3]')
        time.sleep(0.9) #DA TIEMPO
        
        driver.find_element(By.ID, 'codigoPostal').send_keys("080506") #ingresa codigo postal
        Evento.SelectItemDropdownByXpath(driver,'//div[2]/div/p-dropdown/div/span',2) #Documento de débito
        Evento.setValueCheckboxByXpath(driver,'//div[2]/div/div/div[2]/div[2]/p-checkbox/div/div[2]',1) #en esta caso si está activado lo desactiva

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #para que baje todo lo faltante
        time.sleep(2) #DA TIEMPO A QUE BAJE LA PAGINA

        Evento.SelectItemDropdownByXpath(driver,'//div[3]/div/p-dropdown/div/span',1) #Tipo descuento
        driver.find_element(By.XPATH, '//p-inputnumber/span/input').clear() #borra campo Descuento, es vital esto para que funcione la siguiente linea
        driver.find_element(By.XPATH, '//p-inputnumber/span/input').send_keys(15.34) #ingresa Descuento
        Evento.SelectItemDropdownById(driver,'formaPago',2)         #ingresa forma de pago

        #controla modal de Banco
        Evento.ControlModalByXpath(driver,'//div[4]/div[2]/app-dropdown/div/button/span',
                                   '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner',
                                   '/html/body/p-dynamicdialog/div/div/div[2]/app-empresa-dialog/app-spinner',
                                   '//th[3]/p-columnfilter/div/p-columnfilterformelement/input',
                                   'austro','//td[3]')
        
        driver.find_element(By.ID, 'responsablePago').send_keys("el responsable Pago") #ingresa responsable Pago
        driver.find_element(By.ID, 'telefonoCelular').send_keys("0987654321") #ingresa celular
        driver.find_element(By.ID, 'depResponsablePago').send_keys("dep responsable Pago") #ingresa departamento responsable Pago
        driver.find_element(By.ID, 'direccionRetiroCheque').send_keys("Direccion del cheque") #ingresa dirección del cheque

        Evento.SelectItemDropdownById(driver,'pr_id_14_label',4)         #ingresa Periodicidad

        driver.find_element(By.XPATH , '//form/div[2]/button').click()  #guarda el contrato

        Evento.ManageSpinnerByXpath(driver, '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/app-spinner')
        #obtiene numero de contrato
        NContrato=Evento.GetValueInputDisabledByXpath(driver, '/html/body/app-root/app-content-layout/div/app-contrato-empresarial-edit/p-panel/div/div[2]/div/div/p-tabview/div/div[2]/p-tabpanel[1]/div/app-contrato-empresarial-info-edit/form/p-panel[1]/div/div[2]/div/div/div[3]/input')
        print("se generó exitosamente contrato empresarial: "+str(NContrato))
        driver.find_element(By.XPATH , '//img').click()  #sale a pantalla principal
        return NContrato


