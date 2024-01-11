import requests
import time

def initialize_air_quality():

	class SensorMock:
    		def __init__(self):
        		self._ratio = 0
        		self._conc = 0

    		def read(self):
       		 # Simula lecturas del sensor
        		self._ratio += 5
        		self._conc += 100

       			return (24, self._ratio, self._conc)

	# Configuración de ThingsBoard
	thingsboard_host = "http://10.172.117.104:8080"
	access_token = "m3fc4bf6x0g83d7pur9b"

	sensor = SensorMock()

	while True:
    		gpio, ratio, conc = sensor.read()

    		payload = {"air_ratio": round(ratio, 2), "air_concentration": round(conc, 2)}
    		url = f'{thingsboard_host}/api/v1/{access_token}/telemetry'

	    	try:
        		response = requests.post(url, json=payload)
        		response.raise_for_status()
        		print('Datos enviados a ThingsBoard:', payload)
    		except requests.exceptions.RequestException as e:
        		print(f'Error al enviar datos a ThingsBoard: {e}')

    		time.sleep(5)  # Espera 5 segundos antes de la próxima lectura
