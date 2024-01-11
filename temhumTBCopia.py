
import Adafruit_DHT
import requests
import time

def initialize_temp_humidity():

        # Define el tipo de sensor y el número de pin (en este caso, GPIO 24)
        sensor = Adafruit_DHT.DHT11
        pin = 5

        # Configuración de ThingsBoard
        thingsboard_host = "http://10.172.117.104:8080"
        access_token = "m3fc4bf6x0g83d7pur9b"


        while True:
                humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

                if humidity is not None and temperature is not None:
                        payload = {"temperature": round(temperature, 2), "humidity": round(humidity, 2)}

                        url = f'{thingsboard_host}/api/v1/{access_token}/telemetry'

                        try:
                                response = requests.post(url, json=payload)
                                response.raise_for_status()
                                print('Datos enviados a ThingsBoard:', payload)
                        except requests.exceptions.RequestException as e:
                                print(f'Error al enviar datos a ThingsBoard:{e}')

                else:
                        print('Error al leer el sensor.')

                time.sleep(5)  # Espera 5 segundos antes de la próxima lectu>

