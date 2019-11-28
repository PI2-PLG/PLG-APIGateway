import requests as req
import time
import random
import json
import io

quantity_of_collects = 5
interval = 2
localhost = "192.168.15.9"

print(f'Simulando {quantity_of_collects} entradas de dados com intervalo de {interval} segundos entre elas')
for collect in range(1,quantity_of_collects):
    # dados normais
    string_data_A = f'M:Modulo-A,P:{random.randint(200,500)},T:{random.randint(25,33)},U:{random.randint(40,90)},L:{-15.98961},G:{-48.0443975},V:{0}, W:{random.randint(-45,-100)}'
    # modulo desligado
    string_data_B = f'M:Modulo-B,P:{random.randint(200,400)},T:{random.randint(20,38)},U:{random.randint(50,70)},L:{0},G:{0},V:{0}, W:{random.randint(-45,-100)}'
    # risco de incêndio
    string_data_C = f'M:Modulo-C,P:{random.randint(800,800)},T:{random.randint(35,40)},U:{random.randint(10,25)},L:{-15.9906929},G:{-48.0443009},V:{0}, W:{random.randint(-45,-100)}
    # modulo em movimento
    string_data_D = f'M:Modulo-D,P:{random.randint(200,400)},T:{random.randint(25,33)},U:{random.randint(30,60)},L:{-15.9906929},G:{-48.0443009},V:{2}, W:{random.randint(-45,-100)}
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

