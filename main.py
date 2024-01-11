# main.py

import airqualityTBCopia
import temhumTBCopia
import threading

def main():
    # Crear hilos para las funciones de inicialización
    thread_air = threading.Thread(target=airqualityTBCopia.initialize_air_quality)
    thread_temp_hum = threading.Thread(target=temhumTBCopia.initialize_temp_humidity)

    # Iniciar los hilos
    thread_air.start()
    thread_temp_hum.start()

    # Esperar a que ambos hilos terminen
    thread_air.join()
    thread_temp_hum.join()

if __name__ == "__main__":
    main()

