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
    string_data_A = f'M:Modulo-A,P:{random.randint(200,500)},T:{random.randint(25,33)},U:{random.randint(40,90)},L:{0},G:{0},V:{0}, W:{-70}'
    string_data_B = f'M:Modulo-A,P:{random.randint(200,500)},T:{random.randint(30,33)},U:{random.randint(30,80)},L:{0},G:{-48.0443009},V:{0}, W:{-60}'
    string_data_C = f'M:Modulo-A,P:{random.randint(200,500)},T:{random.randint(20,28)},U:{random.randint(35,75)},L:{0},G:{0},V:{0}, W:{-48}'
    string_data_D = f'M:Modulo-A,P:{random.randint(200,500)},T:{random.randint(27,35)},U:{random.randint(25,65)},L:{0},G:{0},V:{0},W:{-52}'
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
