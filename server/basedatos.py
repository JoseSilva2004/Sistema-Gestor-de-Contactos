import contacto
import telefono
import direccion
import sqlite3

class BaseDatos:
    def __init__(self):
        self.__ruta = 'Gestor-Contactos.db'

    def LeerContactos(self):
        try:
            database = sqlite3.connect(self.__ruta)
            cursor = database.cursor()

            cursor.execute("SELECT * FROM Contacto")

            contactos = []

            for registro in cursor:
                contact = contacto.Contacto(registro[0],registro[1],registro[2],registro[3])
                contact.SetListaTelefonos(self.__LeerTelefonos(database,contact.GetId()))
                contact.SetListaDirecciones(self.__LeerDirecciones(database,contact.GetId()))
                contactos.append(contact)

            database.close()
            return contactos
        
        except:
            print("Error: No se pueden leer los datos")
            return []
        
    def __LeerTelefonos(self,database,idcontacto):
        try:
            cursortelefono = database.cursor()
            cursortelefono.execute("SELECT Id, NumeroTelefono,Descripcion FROM Telefono WHERE ContactoId = " + str(idcontacto))

            telefonos = []

            for registro in cursortelefono:
                telefonos.append(telefono.Telefono(registro[0],registro[1],registro[2]))
                return telefonos
            
        except:
            print("Error: No se pueden leer los teléfonos")
            return []
        
    def __LeerDirecciones(self,database,idcontacto):
        try:
            cursordireccion = database.cursor()
            cursordireccion.execute("SELECT Id, Calle, Piso, Ciudad, CodigoPostal FROM Direccion WHERE ContactoId = " + str(idcontacto))

            direcciones = []

            for registro in cursordireccion:
                direcciones.append(direccion.Direccion(registro[0],registro[1],registro[2],registro[3],registro[4]))
            
            return direcciones
        
        except:
            print("Error: No se pueden leer las direcciones")
            return []
        
    def LeerContactosNombre(self,nombre):
        try:
            database = sqlite3.connect(self.__ruta)
            cursor = database.cursor()

            cursor.execute("SELECT * FROM Contacto WHERE nombre = " + nombre + "")

            contactos = []

            for registro in cursor:
                contact = contacto.Contacto(registro[0],registro[1],registro[2],registro[3])
                contact.SetListaTelefonos(self.__LeerTelefonos(database,contact.GetId()))
                contact.SetListaDirecciones(self.__LeerDirecciones(database,contact.GetId()))
                contactos.append(contact)

            database.close()
            return contactos
        
        except:
            print("Error: No se pueden leer contactos por nombre")
            return []
        
    def LeerContactosTelefono(self,telefono):
        try:
            database = sqlite3.connect(self.__ruta)
            cursor = database.cursor()

            cursor.execute("SELECT DISTINCT * FROM WHERE NumeroTelefono = " + telefono + "")

            contactos = []

            for registro in cursor:
                cursorcontacto = database.cursor()
                cursorcontacto.execute("SELECT * FROM Contacto WHERE Id = "+ str(registro[1]))

                for registrocontacto in cursorcontacto:
                    contact = contacto.Contacto(registrocontacto[0],registrocontacto[1],registrocontacto[2],registrocontacto[3])
                    contact.SetListaTelefonos(self.__LeerTelefonos(database,contact.GetId()))
                    contact.SetListaDirecciones(self.__LeerDirecciones(database,contact.GetId()))

                    contactos.append(contact)

            database.close()
            return contactos
            
        except:
            print("Error: No se pueden leer los contactos por teléfono")
            return[]
        
    def InsertarContacto(self,contacto):
        try:
            database = sqlite3.connect(self.__ruta)
            cursor = database.cursor()
            
            infocontacto = (contacto.GetNombre(),contacto.GetApellido(),contacto.GetFechaNacimiento())
            cursor.execute("INSERT INTO Contacto(Nombre,Apellido,FechaNacimiento) VALUES (?,?,?)", infocontacto)

            contactoid = cursor.lastrowid

            for telefono in contacto.GetListaTelefonos():
                infocontacto = (contactoid,telefono.GetNumeroTelefono(),telefono.GetDescripcion())
                cursor.execute("INSERT INTO Telefono (ContactoId,NumeroTelefono,Descripcion) VALUES (?,?,?)", infocontacto)

            for direccion in contacto.GetListaDirecciones():
                infodireccion = (contactoid,direccion.GetCalle(),direccion.GetPiso(),direccion.GetCiudad(),direccion.GetCodigoPostal())
                cursor.execute("INSERT INTO Direccion (ContactoId,Calle,Piso,Ciudad,CodigoPostal) VALUES (?,?,?,?,?)", infodireccion)
                
            database.commit()
            return True
            
        except:
            print("Error: No se puede insertar el contacto")
            return False
        
    def BorrarContactoId(self,idcontacto):
        try:
            database = sqlite3.connect(self.__ruta)
            cursor = database.cursor()

            cursor.execute("DELETE FROM Telefono WHERE ContactoId = " +str(idcontacto))
            cursor.execute("DELETE FROM Direccion WHERE ContactoId = " +str(idcontacto))
            cursor.execute("DELETE FROM Contacto WHERE Id = " + str(idcontacto))

            database.commit()
            return True
        
        except:
            print("Error: No se puede borrar el contacto")
            return False