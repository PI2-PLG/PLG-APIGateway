import requests as req
import time
import random
import json
import io

quantity_of_collects = 5
interval = 5
localhost = "loboguara.eastus.cloudapp.azure.com"

print(f'Simulando {quantity_of_collects} entradas de dados com intervalo de {interval} segundos entre elas')
for collect in range(1,quantity_of_collects):
    string_data_A = f'M:Modulo-A,P:{800},T:{random.randint(36,42)},U:{random.randint(20,50)},L:{-15.98961},G:{-48.0443975},V:{0}, W:{-70}'
    string_data_B = f'M:Modulo-A,P:{800},T:{random.randint(34,45)},U:{random.randint(15,45)},L:{-15.9906929},G:{-48.0443009},V:{0}, W:{-60}'
    string_data_C = f'M:Modulo-A,P:{800},T:{random.randint(32,38)},U:{random.randint(20,30)},L:{-15.9906929},G:{-48.0443009},V:{0}, W:{-48}'
    string_data_D = f'M:Modulo-A,P:{800},T:{random.randint(30,36)},U:{random.randint(15,37)},L:{-15.9941734},G:{-48.0460925},V:{0},W:{-52}'
    module_data_request_A = {"payload":string_data_A}
    module_data_request_B = {"payload":string_data_B}
    module_data_request_C = {"payload":string_data_C}
    module_data_request_D = {"payload":string_data_D}
    response_A = req.post("http://"+localhost+":8000/new-module-data/", json=module_data_request_A)
    response_B = req.post("http://"+localhost+":8000/new-module-data/", json=module_data_request_B)
    response_C = req.post("http://"+localhost+":8000/new-module-data/", json=module_data_request_C)
    response_D = req.post("http://"+localhost+":8000/new-module-data/", json=module_data_request_D)
    print(f"Coleta numero: {collect}")
    time.sleep(interval)
