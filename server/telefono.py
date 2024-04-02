class Telefono:
    def __init__(self,idtelefono,numerotelefono,descripcion):
        self.__Id = idtelefono
        self.__NumeroTelefono = numerotelefono
        self.__Descripcion = descripcion

    def GetId(self):    #Devuelve el identificador del teléfono
        return self.__Id
    
    def GetNumeroTelefono(self):    #Devuelve el número de teléfono
        return self.__NumeroTelefono
    
    def GetDescripcion(self):   #Devuelve la descripción del número de teléfono
        return self.__Descripcion
    
    def SetNumeroTelefono(self,telefono):   #Modifica el valor del número de télefono
        self.__NumeroTelefono = telefono

    def SetDescripcion(self,descripcion):   #Modifica la descripcion del número de teléfono
        self.__Descripcion = descripcion