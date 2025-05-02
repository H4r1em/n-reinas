# cliente.py
import socket

HOST = '127.0.0.1'
PORT = 3000

def query(mensaje: str) -> str:
    """
    Abre un socket, envía mensaje+"\n", lee hasta el primer '\n',
    y devuelve la línea recibida (sin esperar a que el servidor cierre).
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(mensaje.encode() + b'\n')
        recibido = b''
        while b'\n' not in recibido:
            trozo = s.recv(4096)
            if not trozo:
                # conexión cerrada inesperadamente
                break
            recibido += trozo
        # Sólo devolvemos hasta el '\n'
        linea, _sep, _rest = recibido.partition(b'\n')
    return linea.decode()
