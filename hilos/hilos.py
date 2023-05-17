import threading
import time

espera = 0

mensajes = [
    "Hola UK",
    "Procesando",
    "Adiós UK"
]

def mostrar(ms, espera):
    time.sleep(espera)
    print(ms)



for ms in mensajes:
    ejecutar = threading.Thread(target=mostrar, args=(ms, espera))
    espera += 5
    ejecutar.start()