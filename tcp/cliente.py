
import socket
try:
    print('Conectando al servidor')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 6190)
    sock.connect(server_address)
    sock.sendall(b"Hola a todos UK")
finally:
    print("Conexión cerrada.")