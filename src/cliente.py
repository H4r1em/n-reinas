from socket import socket, error, gaierror,AF_INET,SOCK_STREAM,gethostbyname
import sys  
import time

host = 'localhost'
port = 3000
s = None

print('Creando socket')
try:
    s = socket(AF_INET, SOCK_STREAM)
except error:
    print('Error al crear el socket')
    sys.exit()

print('Obteniendo dir ip')
try:
    remote_ip = gethostbyname( host )
except gaierror:
    print('Error, direccion no encontrada')
    sys.exit()

# Conectandose al sistema
print(f'Conectandose al servidor {host} en el puerto {port}')
s.connect((remote_ip , port))

def query(elem):
#    emoji = bytes([0xF0, 0x9F ,0xA4 ,0xA3])
    query = bytearray(f'{elem}\n','UTF8') # dos lineas
    # query.append(13)
    try:
        s.sendall(query)
    except error:
        print('Error de comunicacion')
    reply = s.recv(1024)
    print(f'Lei {reply}')
    reply = reply.decode()
    # while not '\n' in reply:
    #     res = self.s.recv(256)
    #     reply = reply + res.decode()
    return reply



n = input('Dame una cadena:')
while n != 'fin':
    r = query(n)
    print(f'recibi {r}')
    n = input('Dame una cadena:')

s.close()
print("Eso es todo")