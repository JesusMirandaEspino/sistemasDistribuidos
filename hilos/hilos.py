import threading
import time

def mostrar(ms, espera):
    time.sleep(espera)
    print(ms)

mensajes = [
    "Hola UK",
    "Procesando",
    "Adiós UK"
]

espera = 0

for ms in mensajes:
    ejecutar = threading.Thread(target=mostrar, args=(ms, espera))
    espera += 5
    ejecutar.start()