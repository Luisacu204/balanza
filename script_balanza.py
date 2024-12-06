import serial

# Configuración del puerto serie
port = 'COM3'  # Cambia esto según tu sistema (e.g., COM1 en Windows)
baudrate = 9600
parity = serial.PARITY_EVEN
stopbits = serial.STOPBITS_ONE
bytesize = serial.SEVENBITS

# Establecer conexión
ser = serial.Serial(port, baudrate=baudrate, parity=parity, stopbits=stopbits, bytesize=bytesize, timeout=1)

try:
    # Enviar comando para solicitar peso
    ser.write(b'W\r')
    # Leer la respuesta
    response = ser.readline().decode('ascii').strip()
    print(f"Peso recibido: {response}")
except Exception as e:
    print(f"Error en la comunicación: {e}")
finally:
    ser.close()


# import serial

# # Configuracion del puerto de serie que no conosco supongo COM3 segun yo.
# port = "COM3"  # Cambiar
# baud_rate = 9600  # Ajustar segun la configuracion de la banaza para que funcione / 115200 / 1200 /2400 / 4800 

# try:
#     with serial.Serial(port, baud_rate, timeout=1) as ser:
#         print(f"Conectado a la balanza en el puerto {port}")

#         while True:
#             line = ser.readline().decode('utf-8').strip()
#             if line:
#                 print(f"Peso: {line}")
# except serial.SerialException as e:
#     print(f"Error al conectar con la balanza: {e}")
# except KeyboardInterrupt:
#     print("\nCerrando el programa.")

#------------------------------------------------------------------------------------------------
# import serial
# import serial.tools.list_ports

# def find_scale():
#     ports = serial.tools.list_ports.comports()
#     baud_rates = [9600, 115200, 4800]
#     for port in ports:
#         print(f"Puerto detectado: {port.device} ({port.description})")
#         for baud_rate in baud_rates:
#             try:
#                 print(f"Probando puerto {port.device} con baud_rate {baud_rate}")
#                 ser = serial.Serial(port.device, baud_rate, timeout=2)
#                 ser.write(b'\n') 
#                 data = ser.readline()
#                 if data:
#                     print(f"Balanza detectada en {port.device} con baud_rate {baud_rate}")
#                     return ser
#                 ser.close()
#             except (serial.SerialException, FileNotFoundError) as e:
#                 print(f"Error en {port.device} con baud_rate {baud_rate}: {e}")
#     return None

# if __name__ == "__main__":
#     print("Buscando balanza...")
#     scale = find_scale()
#     if scale:
#         print("Conexión exitosa. Leyendo datos...")
#     else:
#         print("No se detectó ninguna balanza.")

# import serial
# import serial.tools.list_ports
# import time

# def find_scale():
#     ports = serial.tools.list_ports.comports()
#     baud_rates = [9600, 115200, 4800]
#     for port in ports:
#         print(f"Puerto detectado: {port.device} ({port.description})")
#         for baud_rate in baud_rates:
#             try:
#                 print(f"Probando puerto {port.device} con baud_rate {baud_rate}")
#                 ser = serial.Serial(port.device, baud_rate, timeout=2)
#                 time.sleep(2)  # Pausa para inicialización
#                 ser.write(b'\n')  # Comando inicial (ajustar según la balanza)
#                 data = ser.readline()
#                 if data:
#                     print(f"Balanza detectada en {port.device} con baud_rate {baud_rate}")
#                     return ser
#                 ser.close()
#             except (serial.SerialException, FileNotFoundError) as e:
#                 print(f"Error en {port.device} con baud_rate {baud_rate}: {e}")
#     return None

# if __name__ == "__main__":
#     print("Buscando balanza...")
#     scale = find_scale()
#     if scale:
#         print("Conexión exitosa. Leyendo datos...")
#     else:
#         print("No se detectó ninguna balanza.")
