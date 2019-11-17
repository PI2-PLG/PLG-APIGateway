from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from endpoints.models import Endpoint
from endpoints.helper import convertCentralData
from rest_framework.permissions import AllowAny
import json
import requests as req
import io


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

    def post(self, request):
        print("")
        print("")
        print("=============================================")
        print("REQUEST:")
        print(request.data)
        print("=============================================")
        print("")
        print("")
        '''
        Exemplo de string de dados
        data = "M:Modulo-Z,P:223,T:23.24,U:24.34,L:234.2223,G:234.2223,V:23.23"
        '''

        data = request.data["payload"]
        module_data = convertCentralData(data)
        module = {"name":module_data["module"]}
        final_response = ""
        try:
            newModule = Endpoint.objects.get(name="NewModule")
            aux = {"module":module}
            response = req.post(newModule.url, json=aux)
        except:
            final_response = {'response':'find_or_create_module_error'}
            return Response(final_response, status=status.HTTP_200_OK)

        try:
            module_data_request = {}
            newData = {
                        "latitude":module_data["latitude"],
                        "longitude":module_data["longitude"],
                        "temperature":module_data["temperature"],
                        "humidity":module_data["humidity"],
                        "ppm":module_data["ppm"],
                        "velocity":module_data["velocity"],
                      }
            module_data_request["module"] = module
            module_data_request["module_data"] = newData
        except:
            final_response = {'response':'find_or_create_module_data_error'}
            return Response(final_response, status=status.HTTP_200_OK)

        try:
            endpoint = Endpoint.objects.get(name="GetAllModuleData")
        except:
            final_response = {'response':'endpoint_not_found'}
            return Response(final_response, status=status.HTTP_200_OK)

        try:
            newModule = Endpoint.objects.get(name="NewModuleData")
            response = req.post(newModule.url, json=module_data_request)
            if(response.text == '{"response":"module-data_successfully_created"}'):
                final_response = {'response':'new_data_saved'}
            else:
                final_response = {'response':'new_data_is_not_saved'}
            return Response(final_response, status=status.HTTP_200_OK)
        except:
            final_response = {'response':'new_data_is_not_saved'}
            return Response(final_response, status=status.HTTP_200_OK)