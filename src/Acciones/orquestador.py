from src.Modulos.Contratos import contratoReg
from src.Modulos.Afiliaciones import afiliacionReg, afiliacionEdit

import pandas as pd

class Orquestador:
    SecuencialContrato=[] #inicializo la matriz q contendrá los numeros de contratos
    CantidadContratos=0

    def CargaDatos(nombre_hoja):
        # Especifica la ruta de tu archivo Excel
        ruta_excel = "Cargadatospreviex.xlsx"
        # Lee el archivo Excel en un DataFrame de pandas
        datos = pd.read_excel(ruta_excel, sheet_name=nombre_hoja)
        # Muestra los primeros registros del DataFrame
        #print(datos.head())
        return datos
    
    def Dirige(self, driver):
        ListaContratos= self.CargaDatos("Contratos") #carga el DataFrame
        if len(ListaContratos)>0: #si hay más de una fila...
            contratoReg.Contrato().UbicarPantalla(driver) #se ubica en la pantalla de contratos
            for indice, fila in ListaContratos.iterrows():
                # 'fila' es una Serie que contiene los datos de la fila
                diccionario_fila = fila.to_dict() #crea un diccionario en base de la fila iterada del dataframe
                
                NContrato=contratoReg.Contrato().Registrar(driver,diccionario_fila)
                print('Listo para agregar afiliaciones al contrato '+str(NContrato))
                self.SecuencialContrato.append([0]*2) #agrego dos columnas a las filas
                self.SecuencialContrato[indice][0] = indice + 1 #orden de creación de contrato
                self.CantidadContratos = indice + 1 #contar contratos
                self.SecuencialContrato[indice][1] = NContrato  #numero de contrato

            contratoReg.Contrato().Salir(driver) #sale a pantalla principal
            del ListaContratos # Eliminar el DataFrame y liberar memoria

        ListaAfiliaciones= self.CargaDatos("Afiliaciones") #carga el DataFrame
        if len(ListaAfiliaciones)>0: #si hay más de una fila...
                        #ABRIR VENTANA DE AFILIACIONES
            for f in range(self.CantidadContratos-1): #recorre por la cantidad de contratos creados
                SubListaAfil=ListaAfiliaciones.loc[ListaAfiliaciones['Ncontrato'] == f] #crea un subdataFrame por las afiliaciones creadas para cada contrato
                if len(SubListaAfil)>0: #si hay más de una fila...
                    for indice, fila in SubListaAfil.iterrows():
                        diccionario_fila = fila.to_dict() #crea un diccionario en base de la fila iterada del dataframe
                        NAiliacion=afiliacionReg.Afiliacion().Registrar(driver,self.SecuencialContrato[f][1],diccionario_fila)

                        #falta ahora hacer las validaciones de que si hay beneficiarios... y adicionales

    

