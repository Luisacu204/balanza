import serial

port = "COM3"  # Cambiar al puerto correcto
baud_rate = 9600  # Ajustar según la configuración de la balanza

try:
    with serial.Serial(port, baud_rate, timeout=5) as ser:
        print(f"Conectado a la balanza en el puerto {port}")

        # Si necesitas enviar un comando inicial, descomenta:
        # ser.write(b'\r\n')

        while True:
            raw_data = ser.readline()
            print(f"Datos crudos: {raw_data}")  # Depuración de datos sin procesar

            if raw_data:
                try:
                    decoded_data = raw_data.decode('utf-8', errors='ignore').strip()
                    if decoded_data:  # Solo muestra si no está vacío
                        print(f"Peso detectado: {decoded_data}")
                except UnicodeDecodeError:
                    print(f"Error al decodificar: {raw_data}")
            else:
                print("Sin datos... esperando entrada.")
except serial.SerialException as e:
    print(f"Error al conectar con la balanza: {e}")
except KeyboardInterrupt:
    print("\nCerrando el programa.")
