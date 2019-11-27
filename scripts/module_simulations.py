import requests as req
import time
import random
import json
import io

quantity_of_collects = 7
interval = 2
localhost = "192.168.15.9"

print(f'Simulando {quantity_of_collects} entradas de dados com intervalo de {interval} segundos entre elas')
for collect in range(1,quantity_of_collects):
    string_data_A = f'M:Modulo-A,P:{random.randint(200,500)},T:{random.randint(25,40)},U:{random.randint(40,90)},L:{-15.990043},G:{-48.046277},V:{0}, W:{random.randint(-45,-100)}'
    string_data_B = f'M:Modulo-B,P:{random.randint(200,500)},T:{random.randint(20,38)},U:{random.randint(30,70)},L:{-15.990846},G:{-48.045164},V:{0}, W:{random.randint(-45,-100)}'
    string_data_C = f'M:Modulo-C,P:{random.randint(200,500)},T:{random.randint(15,35)},U:{random.randint(15,40)},L:{-15.989804},G:{-48.043127},V:{0}, W:{random.randint(-45,-100)}
    string_data_D = f'M:Modulo-D,P:{random.randint(200,500)},T:{random.randint(17,37)},U:{random.randint(10,30)},L:{-15.988280},G:{-48.044277},V:{0}, W:{random.randint(-45,-100)}
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
