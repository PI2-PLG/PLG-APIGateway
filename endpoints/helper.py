from endpoints.models import Endpoint
from users.models import CustomUser
import requests as req
import json
import io

def convert_central_data(payload):
    '''
        M: => Modulo
        P: => Partículas por Milhão
        T: => Temperatura
        U: => Umidade
        L: => Latitude
        G: => Longitude
        V: => Velocidade
        W: => Força do Sinal
    '''
    data = payload.split(",")
    module_data = {}
    for value in data:
        aux_value = value.split(":")
        if(aux_value[0] == "M"):
            module_data["module"] = aux_value[1]
        elif(aux_value[0] == "P"):
            module_data["ppm"] = aux_value[1]
        elif(aux_value[0] == "T"):
            module_data["temperature"] = aux_value[1]
        elif(aux_value[0] == "U"):
            module_data["humidity"] = aux_value[1]
        elif(aux_value[0] == "L"):
            module_data["latitude"] = aux_value[1]
        elif(aux_value[0] == "G"):
            module_data["longitude"] = aux_value[1]
        elif(aux_value[0] == "V"):
            module_data["velocity"] = aux_value[1]
        elif(aux_value[0] == "W"):
            module_data["signal_strength"] = aux_value[1]

    return module_data

def send_notification(module_name):
    print(module_name)
    final_response = ""
    try:
        all_data_endpoint = Endpoint.objects.get(name="GetAllData")
        response = req.get(all_data_endpoint.url)
        modules_and_status = []
        for module in response.json():
            aux = {}
            if(module["name"] == module_name):
                aux["module_name"] = module["name"]
                aux["module_status"] = module["status"]
                modules_and_status.append(aux)
        notification_pack = {}
        notification_pack["modules"] = modules_and_status
        notification_pack["notification_tokens"] = get_all_notification_tokens()
        notification_endpoint = Endpoint.objects.get(name="SendingNotificationData")
        req.post(notification_endpoint.url, json=notification_pack)
        print("[LOG] Sending notification data to notification service.")
    except:
        print("[LOG] Impossible send notification to notification service.")

def get_all_notification_tokens():
    users = CustomUser.objects.all().values('notification_token').distinct()
    tokens = []
    for user in users:
        tokens.append(user["notification_token"])
    return tokens
