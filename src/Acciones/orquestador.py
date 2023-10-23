from src.Modulos.Contratos import contratoReg
from src.Modulos.Afiliaciones import afiliacionReg

class Orquestador:
    def Dirige(self, driver):
        #contratoReg.Contrato().Registrar(driver)
        afiliacionReg.Afiliacion().Registrar(driver)
