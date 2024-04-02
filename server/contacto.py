import telefono
import direccion

class Contacto:
    def __init__(self,idcontacto,nombre,apellido,fechanacimiento):
        self.__Id = idcontacto
        self.__Nombre = nombre
        self.__Apellido = apellido
        self.__FechaNacimiento = fechanacimiento
        self.__ListaTelefonos = []
        self.__ListaDirecciones = []

    def GetId(self):
        return self.__Id
    
    def GetNombre(self):
        return self.__Nombre
    
    def GetApellido(self):
        return self.__Apellido
    
    def GetFechaNacimiento(self):
        return self.__FechaNacimiento
    
    def GetListaTelefonos(self):
        return self.__ListaTelefonos
    
    def GetListaDirecciones(self):
        return self.__ListaDirecciones
    
    def SetNombre(self,nombre):
        self.__Nombre = nombre

    def SetApellido(self,apellido):
        self.__Apellido = apellido

    def SetFechaNacimiento(self,fechanacimiento):
        self.__FechaNacimiento = fechanacimiento

    def SetListaTelefonos(self,listatelefonos):
        self.__ListaTelefonos = listatelefonos

    def SetListaDirecciones(self,listadirecciones):
        self.__ListaDirecciones = listadirecciones
