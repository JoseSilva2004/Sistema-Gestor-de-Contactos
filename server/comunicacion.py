import socket
import basedatos
import contacto
import telefono
import direccion
import conversion

def HiloCliente(conexion,direccion):
    fin = False
    while not fin:
        try:
            recibido = conexion.recv(1024)
            recibido = recibido.decode('utf-8')

            print("Comando recibido: ", recibido)

            if recibido == "5":
                fin = True

            mensaje = str(ProcesarMensaje(recibido))
            conexion.send(str.encode(mensaje))

        except:
            print("Error: Hilo cliente")
            fin = True
    conexion.close()

def ProcesarMensaje(mensaje):
    try:
        listamensaje = mensaje.split('&')
        #Buscar contacto por nombre
        if listamensaje[0] == "1" and listamensaje[1] == "1":
            return BuscarContactoNombre(listamensaje[2])

        #Buscar contacto por teléfono
        if listamensaje[0] == "1" and listamensaje[1] == "2":
            return BuscarContactoTelefono(listamensaje[2])

        if listamensaje[0] == "2":
            return CrearContacto(listamensaje[1])

        if listamensaje[0] == "3" and listamensaje[1] == "1":
            return BorrarContactoNombre(listamensaje[2])

        if listamensaje[0] == "3" and listamensaje[1] == "2":
            return BorrarContactoTelefono(listamensaje[2])

        if listamensaje[0] == "4":
            return BuscarTodosLosContactos()

    except:
        print("Error: Procesando el mensaje recibido")
        return ""


def CrearContacto(contactostring):
    contacto = conversion.StringAContacto(contactostring.lstrip("*"))
    database = basedatos.BaseDatos()
    
    if database.InsertarContacto(contacto) == True:
        return "1"
    else:
        return "0"
    
def BuscarTodosLosContactos():
    database = basedatos.BaseDatos()
    datos = database.LeerContactos()

    if len(datos) > 0:
        return conversion.ContactosAString(datos)
    else:
        return "0"
    
def BuscarContactoNombre(nombre):
    database = basedatos.BaseDatos()
    datos = database.LeerContactosNombre(nombre)

    if len(datos) > 0:
        return conversion.ContactosAString(datos)
    else:
        return "0"
    
def BuscarContactoTelefono(telefono):
    database = basedatos.BaseDatos()
    datos = database.LeerContactosTelefono(telefono)

    if len(datos) > 0:
        return conversion.ContactosAString(datos)
    else:
        return "0"
    
def BorrarContactoNombre(nombre):
    database = basedatos.BaseDatos()
    datos = database.LeerContactosNombre(nombre)
    respuesta = "1"

    for contacto in datos:
        if database.BorrarContactoId(contacto.GetId()) == False:
            respuesta = "0"

    return respuesta

def BorrarContactoTelefono(telefono):
    database = basedatos.BaseDatos()
    datos = database.LeerContactosTelefono(telefono)
    respuesta = "1"

    for contacto in datos:
        if database.BorrarContactoId(contacto.GetId()) == False:
            respuesta = "0"

    return respuesta


