from src.Modulos.Contratos import contratoReg
from src.Modulos.Afiliaciones import afiliacionReg, afiliacionEdit

class Orquestador:
    def Dirige(self, driver):
        NContrato=323
        #NContrato=contratoReg.Contrato().Registrar(driver)
        print('Listo para agregar afiliaciones al contrato '+str(NContrato))
        afiliacionReg.Afiliacion().Registrar(driver,NContrato)
        #afiliacionEdit.Afiliacion().Editar(driver,NContrato)
