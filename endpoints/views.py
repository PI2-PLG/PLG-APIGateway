from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from endpoints.models import Endpoint
from endpoints.helper import convert_central_data, send_notification, temp_med, ppm_med, hum_med
from rest_framework.permissions import AllowAny
import json
import requests as req
import io


class ModulesToMap(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            endpoint = Endpoint.objects.get(name="GetAllData")
        except:
            return Response({'response':'endpoint_not_foud'}, status=status.HTTP_200_OK)

        response = req.get(endpoint.url)
        modules = response.json()

        modules_list = []
        for module in modules:
            module_data = {
                            "coordinate":{
                                           "latitude": module["latitude"][-1],
                                           "longitude": module["longitude"][-1],
                                         },
                            "title": module["name"],
                            "status": module["status"],
                            "description": f'Temperatura {module["temperature"][0]} C°, Umidade {module["humidity"][0]} %, Gases: {module["ppm"][0]} ppm, Velocidade: {module["velocity"][-1]} m/s, Potência do Sinal: {module["signal_strength"][-1]}',
                           }
            #print(module["signal_strength"][-1])
            modules_list.append(module_data)
        return Response(modules_list, status=status.HTTP_200_OK)

class GetModuleList(APIView):

    permission_classes = (AllowAny,)

    def get(self,request):
        try:
            endpoint = Endpoint.objects.get(name="GetAllModuleList")
        except:
            return Response({'response': 'endpoint_not_found'}, status=status.HTTP_200_OK)
        try:
            response = req.get(endpoint.url)
            return Response(response.json(), status=status.HTTP_200_OK)
        except:
            return Response({'response': 'no_reply'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

class GetAllData(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            endpoint = Endpoint.objects.get(name="GetAllData")
        except:
            return Response({'response':'endpoint_not_foud'}, status=status.HTTP_200_OK)
        try:
            response = req.get(endpoint.url)
            return Response(response.json(), status=status.HTTP_200_OK)
        except:
            return Response({'response': 'no_reply'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

class GetModule(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            endpoint = Endpoint.objects.get(name="GetAllModuleData")
        except:
            return Response({'response':'endpoint_not_found'}, status=status.HTTP_200_OK)
        try:
            data = {'module':{'name':request.data["module"]["name"]}}
            response = req.get(url=endpoint.url, json=data)
            return Response(response.json(), status=status.HTTP_200_OK)
        except:
            return Response({'response': 'no_reply'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

class PostModuleData(APIView):

    permission_classes = (AllowAny,)

    '''
    Exemplo de string de dados
    data = "M:Modulo-Z,P:223,T:23.24,U:24.34,L:234.2223,G:234.2223,V:23.23"
    '''
    def post(self, request):
        print("")
        print("")
        print("=============================================")
        print("REQUEST STRING:")
        print(request.data)
        print("=============================================")
        print("")
        print("")
        final_response = ""
        '''
        Tenta encontrar o payload na request
        '''
        try:
            data = request.data["payload"]
            module_data = convert_central_data(data)
            module = {"name":module_data["module"]}
        except:
            final_response = {"response":"payload_not_found"}
            return Response(final_response, status=status.HTTP_200_OK)

        '''
        Tenta encontrar ou criar um novo módulo via serviço de BI
        '''
        try:
            newModule = Endpoint.objects.get(name="NewModule")
            aux = {"module":module}
            response = req.post(newModule.url, json=aux)
        except:
            final_response = {'response':'find_or_create_module_error'}
            return Response(final_response, status=status.HTTP_200_OK)

        '''
        Tenta criar um json no formato aceito por ModuleData
        '''
        try:
            module_data_request = {}
            newData = {
                        "latitude":module_data["latitude"],
                        "longitude":module_data["longitude"],
                        "temperature":module_data["temperature"],
                        "humidity":module_data["humidity"],
                        "ppm":module_data["ppm"],
                        "velocity":module_data["velocity"],
                        "signal_strength":module_data["signal_strength"],
                      }
            module_data_request["module"] = module
            module_data_request["module_data"] = newData
        except:
            final_response = {'response':'find_or_create_module_data_error'}
            return Response(final_response, status=status.HTTP_200_OK)

        '''
        Tenta salvar um novo ModuleData via serviço de BI
        '''
        try:
            newModule = Endpoint.objects.get(name="NewModuleData")
            response = req.post(newModule.url, json=module_data_request)
            if(response.text == '{"response":"module-data_successfully_created"}'):
                final_response = {'response':'new_data_saved'}
            else:
                final_response = {'response':'new_data_is_not_saved'}
        except:
            final_response = {'response':'new_data_is_not_saved'}
            return Response(final_response, status=status.HTTP_200_OK)

        '''
        Avisa para o serviço de notification os novos modulos e status
        '''
        send_notification(module_data["module"])

        return Response(final_response, status=status.HTTP_200_OK)

class AllNotifications(APIView):

    def get(self, request):
        try:
            endpoint = Endpoint.objects.get(name="AllNotificationData")
            response = req.get(endpoint.url)
            return Response(response.json(), status=status.HTTP_200_OK)
        except:
            return Response({'response':'endpoint_not_found'}, status=status.HTTP_200_OK)

class AllCharts(APIView):

    def get(self, request):
        try:
            endpoint = Endpoint.objects.get(name="GetAllData")
        except:
            return Response({'response':'endpoint_not_foud'}, status=status.HTTP_200_OK)
        try:
            response = req.get(endpoint.url)
        except:
            return Response({'response': 'no_reply'}, status=status.HTTP_200_OK)

        modules = response.json()

        all_chart_values = []
        for module in modules:
            aux = {}
            aux["module_name"] = module["name"]
            aux["type"] = "bar_chart"
            aux["title"] = f"{module['name']} - Temperatura x Humidade x PPM"

            data = []
            temperatura = {"info":"Temperatura °", "value": module["temperature"][-1]}
            umidade = {"info":"Umidade %", "value": module["humidity"][-1]}
            ppm = {"info":"PPM ", "value": module["ppm"][-1]}
            data.append(temperatura)
            data.append(umidade)
            data.append(ppm)

            aux["data"] = data
            all_chart_values.append(aux)

        modules_names = []
        aux = {}
        aux["module_name"] = "Media"
        aux["type"] = "line_chart"
        aux["title"] = f'Temperatura Média x Módulo'
        data = {}
        data["labels"] = []
        aux_values = []
        dataset_json = {}
        dataset_json["data"] = []
        for module in modules:
            aux_name = module["name"].split("-")
            new_name = aux_name[0][0]+"-"+aux_name[1]
            data["labels"].append(new_name)
            modules_names.append(module["name"])
            dataset_json["data"].append(temp_med(module))
        aux_values.append(dataset_json)
        data["datasets"] = aux_values
        aux["data"] = data
        all_chart_values.append(aux)

        modules_names = []
        aux = {}
        aux["module_name"] = "Media"
        aux["type"] = "line_chart"
        aux["title"] = f'Umidade Média x Módulo'
        data = {}
        data["labels"] = []
        aux_values = []
        dataset_json = {}
        dataset_json["data"] = []
        for module in modules:
            aux_name = module["name"].split("-")
            new_name = aux_name[0][0]+"-"+aux_name[1]
            data["labels"].append(new_name)
            modules_names.append(module["name"])
            dataset_json["data"].append(hum_med(module))
        aux_values.append(dataset_json)
        data["datasets"] = aux_values
        aux["data"] = data
        all_chart_values.append(aux)

        modules_names = []
        aux = {}
        aux["module_name"] = "Media"
        aux["type"] = "line_chart"
        aux["title"] = f'PPM Médio x Módulo'
        data = {}
        data["labels"] = []
        aux_values = []
        dataset_json = {}
        dataset_json["data"] = []
        for module in modules:
            aux_name = module["name"].split("-")
            new_name = aux_name[0][0]+"-"+aux_name[1]
            data["labels"].append(new_name)
            modules_names.append(module["name"])
            dataset_json["data"].append(ppm_med(module))
        aux_values.append(dataset_json)
        data["datasets"] = aux_values
        aux["data"] = data
        all_chart_values.append(aux)

        try:
            endpoint = Endpoint.objects.get(name="AllNotificationData")
            notifications = req.get(endpoint.url)
            notifications = notifications.json()
            # return Response(response.json(), status=status.HTTP_200_OK)
        except:
            return Response({'response':'endpoint_not_found'}, status=status.HTTP_200_OK)


        mod_not = []
        for module in modules_names:
            aux = {}
            qtd_alert = 0
            qtd_off = 0
            qtd_motion = 0
            for notification in notifications:
                if(notification["type"] == "alert" and notification["module_name"] == module):
                    qtd_alert += 1
                elif(notification["type"] == "off" and notification["module_name"] == module):
                    qtd_off += 1
                elif(notification["type"] == "inmotion" and notification["module_name"] == module):
                    qtd_motion += 1
            aux["module"] = module
            aux["alert"] = qtd_alert
            aux["off"] = qtd_off
            aux["inmotion"] = qtd_motion
            mod_not.append(aux)

        f_aux = []
        for value in mod_not:
            pie_chart = {}
            pie_chart["module_name"] = value["module"]
            pie_chart["type"] = "pie_chart"
            pie_chart["title"] = f"{value['module']}- Porcentagem x Status"
            data = []
            alerta = {
                "name": "Alerta",
                "population": value["alert"],
                "color": "#a9eec2",
                "legendFontColor": "#7f7f7f",
                "legendFontSize": 10
            }
            data.append(alerta)
            off = {
                "name": "Offline",
                "population": value["off"],
                "color": "#fad284",
                "legendFontColor": "#7f7f7f",
                "legendFontSize": 10
            }
            data.append(off)
            movimento = {
                "name": "Em movimento",
                "population": value["inmotion"],
                "color": "#f38181",
                "legendFontColor": "#7f7f7f",
                "legendFontSize": 10
            }
            data.append(movimento)
            pie_chart["data"] = data
            all_chart_values.append(pie_chart)

        return Response(all_chart_values,status=status.HTTP_200_OK)

class ModulesCount(APIView):

    def get(self, request):
        try:
            endpoint = Endpoint.objects.get(name="GetAllData")
        except:
            return Response({'response':'endpoint_not_foud'}, status=status.HTTP_200_OK)
        try:
            response = req.get(endpoint.url)
        except:
            return Response({'response': 'no_reply'}, status=status.HTTP_200_OK)

        modules = response.json()

        index = 0
        for module in modules:
            index += 1

        qtd = {}
        qtd["modules_count"] = index

        return Response(qtd, status=status.HTTP_200_OK)
