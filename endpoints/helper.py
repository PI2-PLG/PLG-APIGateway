from endpoints.models import Endpoint
import requests as req
import json
import io

def convertCentralData(payload):
    '''
        M: => Modulo
        P: => Partículas por Milhão
        T: => Temperatura
        U: => Umidade
        L: => Latitude
        G: => Longitude
        V: => Velocidade
    '''
    data = payload.split(",")
    module_data = {}
    for value in data:
        aux_value = value.split(":")
        if(aux_value[0] == "M"):
            module_data["module"] = aux_value[1]
            pass
        elif(aux_value[0] == "P"):
            module_data["ppm"] = aux_value[1]
            pass
        elif(aux_value[0] == "T"):
            module_data["temperature"] = aux_value[1]
            pass
        elif(aux_value[0] == "U"):
            module_data["humidity"] = aux_value[1]
            pass
        elif(aux_value[0] == "L"):
            module_data["latitude"] = aux_value[1]
            pass
        elif(aux_value[0] == "G"):
            module_data["longitude"] = aux_value[1]
            pass
        elif(aux_value[0] == "V"):
            module_data["velocity"] = aux_value[1]
            pass

    return module_data
