import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'Hola a todos UK'

try:
    sent = sock.sendto(message, server_address)
    data, server = sock.recvfrom(4096)
    print('Enviando mensaje')
finally:
    sock.close()