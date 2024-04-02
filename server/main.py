import socket
import threading
import comunicacion

SocketServidor = socket.socket()
host = '127.0.0.1'
puerto = 30000
SocketServidor.bind((host,puerto))

SocketServidor.listen()

print("¡Servidor Arrancado!")

while True:
    cliente, direccion = SocketServidor.accept()
    print('Nuevo cliente conectado: ' + direccion[0] + ':'+ str(direccion[1]))
    hilo = threading.Thread(target=comunicacion.HiloCliente,args=(cliente,direccion[0] + ':' + str(direccion[1]),))
    hilo.start()
    SocketServidor.close()


