import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 6190))
    sock.listen()
    print("Esperando al cliente...")
    conn, address = sock.accept()
    print(f"address[0]:address[1] se ha conectado.")
    while True:
        data = conn.recv(1024)
        if data:
            print("Tu mensaje ha sido recibido", data)
            break
finally:
    print("Conexión cerrada.")