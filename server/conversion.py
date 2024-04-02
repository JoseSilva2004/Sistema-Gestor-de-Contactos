import contacto
import telefono
import direccion

def StringAContacto(cadena):
    try:
        print(cadena)
        #Obtención de los datos del contacto y creacion del objeto con los valores
        datoscontacto = cadena.split("#")[0].split("|")
        contact = contacto.Contacto(0,datoscontacto[0],datoscontacto[1],datoscontacto[2])

        #Obtencion de los telefonos y borrado del primer elemento
        #ya que seria vacio empezar la cadena por #
        datostelefono = cadena.split("#")[1].split("-")
        del datostelefono[0:1]

        if len(datostelefono) > 0:
            telefonos = []
            #Procesamiento de todos los teléfonos y almacenamiento en un lista
            for item in datostelefono:
                telephone = telefono.Telefono(0,item.split("|")[0],item.split("|")[1])
                telefonos.append(telephone)
            #Añade los telefonos al contacto
            contact.SetListaTelefonos(telefonos)
        
        #Obtención de las direcciones y borrado del primer elemento
        #Ya que sría vacío al empezar la cadena por #
        datosdirecciones = cadena.split("#")[2].split("-")
        del datosdirecciones[0:1]

        if len(datosdirecciones) > 0:
            direcciones = []
            #Procesamiento de todas las direcciones y almacenamiento en una lista
            for item in datosdirecciones:
                direction = direccion.Direccion(0,item.split("|")[0],item.split("|")[1],item.split("|")[2],item.split("|")[3])
                direcciones.append(direction)
            
            #Añade las direcciones
            contact.SetListaDirecciones(direcciones)
        return contact
    
    except:
        print("Error: No puede convertirse la cadena a tipo contacto")
        return None 

def ContactosAString(contactos):
    try:
        cadena = ""
        #Cada contacto será insertado en la cadena uno a uno
        for contacto in contactos:
            #Datos del contacto
            cadena += "*"
            cadena += contacto.GetNombre()
            cadena += "|"
            cadena += contacto.GetApellido()
            cadena += "|"
            cadena += contacto.GetFechaNacimiento()
            #Datos de sus telefonos
            cadena += "#"
            listatelefonos = contacto.GetListaTelefonos()
            if type(listatelefonos) != type(None):
                for telefono in listatelefonos:
                    cadena += "-"
                    cadena += str(telefono.GetNumeroTelefono())
                    cadena += "|"
                    cadena += str(telefono.GetDescripcion())

            #Datos de sus direcciones
            cadena += "#"
            listadirecciones = contacto.GetListaDirecciones()
            if type(listadirecciones) != type(None):
                for direccion in listadirecciones:
                    cadena += "-"
                    cadena += str(direccion.GetCalle())
                    cadena += "|"
                    cadena += str(direccion.GetPiso())
                    cadena += "|"
                    cadena += str(direccion.GetCiudad())
                    cadena += "|"
                    cadena += str(direccion.GetCodigoPostal())

        return cadena
    
    except:
        print("Error: No Puede convertirse el tipo contacto a cadena de texto")
        return None
