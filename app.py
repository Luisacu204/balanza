import serial
import time
import re
import threading
import tkinter as tk
from tkinter import messagebox
import pyautogui  # Asegúrate de instalar esta biblioteca con `pip install pyautogui`
import keyboard   # Asegúrate de instalar esta biblioteca con `pip install keyboard`

# Configuración del puerto serial (ajusta según tu puerto)
PUERTO_SERIAL = 'COM6'  # Cambia esto a tu puerto, por ejemplo, '/dev/ttyUSB0' en Linux
BAUD_RATE = 9600        # Asegúrate de que esta es la tasa de baudios correcta para tu balanza

# Intentar abrir el puerto serial
try:
    ser = serial.Serial(PUERTO_SERIAL, BAUD_RATE, timeout=1)
    print(f"Conexión establecida con la balanza en el puerto {PUERTO_SERIAL}")
except serial.SerialException as e:
    print(f"Error al abrir el puerto: {e}")
    

# Función para leer datos del puerto serial y actualizar la etiqueta
def leer_peso():
    while True:
        try:
            # Vacía el búfer de entrada para asegurarte de obtener datos nuevos
            ser.reset_input_buffer()
            time.sleep(0.1)

            if ser.in_waiting > 0:
                datos_brutos = ser.read(ser.in_waiting)
                datos_decodificados = datos_brutos.decode('latin-1', errors='ignore')

                # Expresión regular para encontrar los 4 dígitos después del primer "0"
                patron = r"0(\d{4})"
                coincidencia = re.search(patron, datos_decodificados)

                if coincidencia:
                    four_digits = coincidencia.group(1)
                    cuatro_digitos = int(four_digits)
                    primer_digito = four_digits[0]

                    if primer_digito == '0':    
                        gramos = cuatro_digitos / 1000
                        peso.set(f"{gramos:.3f} gr")  # Actualiza el peso en la etiqueta
                    else:
                        kilogramos = cuatro_digitos / 1000
                        peso.set(f"{kilogramos:.3f} kg")  # Actualiza el peso en la etiqueta
                else:
                    peso.set("No se encontró el peso")
            else:
                peso.set("No hay datos disponibles")

            time.sleep(0.5)  # Retardo para evitar saturación
        except Exception as e:
            peso.set(f"Error: {e}")

# Función para simular la escritura del peso en el teclado con coma en lugar de punto
def enviar_al_teclado():
    try:
        peso_actual = peso.get()
        # Extraer solo los números del peso (sin "gr" o "kg")
        peso_numerico = re.search(r"[\d.]+", peso_actual)
        if peso_numerico:
            # Reemplaza el punto por una coma
            peso_formateado = peso_numerico.group().replace('.', ',')
            pyautogui.write(peso_formateado, interval=0.2)  # Escribe el peso con coma y más lentamente
            print(f"Peso '{peso_formateado}' enviado al teclado con coma.")
        else:
            print("No hay un peso válido para enviar.")
    except Exception as e:
        print(f"Error al enviar el peso al teclado: {e}")

# Función para detectar la tecla física Insert y enviar el peso al teclado
def detectar_tecla():
    while True:
        if keyboard.is_pressed('insert'):  # Detecta si se presiona la tecla Insert
            enviar_al_teclado()
            time.sleep(0.5)  # Retardo para evitar múltiples activaciones

# Función para cerrar la aplicación y liberar el puerto serial
def cerrar_aplicacion():
    if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
        ser.close()
        root.destroy()

# Crear la ventana principal de tkinter
root = tk.Tk()
root.title("Visualizador de Peso")
root.geometry("300x250")
root.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)

# Hacer que la ventana siempre esté encima
root.attributes("-topmost", True)

# Etiqueta para mostrar el peso
peso = tk.StringVar()
peso.set("Esperando datos...")
etiqueta_peso = tk.Label(root, textvariable=peso, font=("Helvetica", 16))
etiqueta_peso.pack(pady=20)

# Inicia el hilo para leer datos del puerto serial
hilo_lectura = threading.Thread(target=leer_peso, daemon=True)
hilo_lectura.start()

# Inicia el hilo para detectar la tecla Insert
hilo_tecla = threading.Thread(target=detectar_tecla, daemon=True)
hilo_tecla.start()

# Ejecuta el bucle principal de tkinter
root.mainloop()
