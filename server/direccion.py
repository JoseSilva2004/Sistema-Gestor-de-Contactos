class Direccion:
    def __init__(self,iddireccion,calle,piso,ciudad,codigopostal):
        self.__Id = iddireccion
        self.__Calle = calle
        self.__Piso = piso
        self.__Ciudad = ciudad
        self.__CodigoPostal = codigopostal

    def GetId(self):
        return self.__Id
    
    def GetCalle(self):
        return self.__Calle
    
    def GetPiso(self):
        return self.__Piso
    
    def GetCiudad(self):
        return self.__Ciudad
    
    def GetCodigoPostal(self):
        return self.__CodigoPostal
    
    def SetCalle(self,calle):
        self.__Calle = calle

    def SetPiso(self,piso):
        self.__Piso = piso

    def SetCiudad(self,ciudad):
        self.__Ciudad = ciudad

    def SetCodigoPostal(self,codigopostal):
        self.__CodigoPostal = codigopostal