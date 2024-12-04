import serial

# Configuracion del puerto de serie que no conosco supongo COM3 segun yo.
port = "COM3"  # Cambiar
baud_rate = 9600  # Ajustar segun la configuracion de la banaza para que funcione / 115200

try:
    with serial.Serial(port, baud_rate, timeout=1) as ser:
        print(f"Conectado a la balanza en el puerto {port}")

        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"Peso: {line}")
except serial.SerialException as e:
    print(f"Error al conectar con la balanza: {e}")
except KeyboardInterrupt:
    print("\nCerrando el programa.")

#------------------------------------------------------------------------------------------------
# import serial
# import serial.tools.list_ports

# def find_scale():
#     ports = serial.tools.list_ports.comports()
#     baud_rates = [9600, 115200, 4800]
#     for port in ports:
#         for baud_rate in baud_rates:
#             try:
#                 print(f"Probando puerto {port.device} con baud_rate {baud_rate}")
#                 ser = serial.Serial(port.device, baud_rate, timeout=1)
#                 ser.write(b'\n')  # Algunos dispositivos requieren un comando inicial
#                 data = ser.readline().decode('utf-8').strip()
#                 if data:
#                     print(f"Balanza detectada en {port.device} con baud_rate {baud_rate}")
#                     return ser  # Devuelve el objeto Serial conectado
#                 ser.close()
#             except (serial.SerialException, UnicodeDecodeError):
#                 continue
#     return None

# def read_scale(serial_connection):
#     try:
#         while True:
#             line = serial_connection.readline().decode('utf-8').strip()
#             if line:
#                 print(f"Peso: {line}")
#     except KeyboardInterrupt:
#         print("\nCerrando conexión.")
#     finally:
#         serial_connection.close()

# if __name__ == "__main__":
#     print("Buscando balanza...")
#     scale = find_scale()
#     if scale:
#         print("Conexión exitosa. Leyendo datos...")
#         read_scale(scale)
#     else:
#         print("No se detectó ninguna balanza.")
