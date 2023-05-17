import threading
import time

def mostrar(ms, espera):
    time.sleep(espera)
    print(ms)

mensajes = [
    ("Hola UK", 0),
    ("Procesando", 5),
    ("Adiós UK", 10)
]

for ms, espera in mensajes:
    ejecutar = threading.Thread(target=mostrar, args=(ms, espera))
    ejecutar.start()