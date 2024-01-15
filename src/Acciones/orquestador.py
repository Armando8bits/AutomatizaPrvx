from src.Modulos.Contratos import contratoReg
from src.Modulos.Afiliaciones import afiliacionReg, afiliacionEdit

class Orquestador:
    def Dirige(self, driver):
        for i in range(1, 11): #bucle del 1 al 10
            print ("Inicio del CONTRATO #"+str(i))
            contratoReg.Contrato().Registrar(driver)
        #afiliacionReg.Afiliacion().Registrar(driver)
        #afiliacionEdit.Afiliacion().Editar(driver)
