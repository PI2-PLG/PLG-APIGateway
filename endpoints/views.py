from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from endpoints.models import Endpoint
from endpoints.helper import convertCentralData
import json
import requests as req
import io


class GetModuleList(APIView):

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

    def post(self, request):
        '''
            M: => Modulo
            P: => Partículas por Milhão
            T: => Temperatura
            U: => Umidade
            L: => Latitude
            G: => Longitude
            V: => Velocidade
        '''

        # fazer a requisição receber de request

        data = "M:Modulo-A,P:223,T:23.24,U:24.34,L:2234.2322,G:234,2223,V:23.23"
        module_data = convertCentralData(data)
        print(module_data)

        # verificar se o modulo existe
        module = {"module":module_data["module"]}
        print(module)
        # se o modulo existir, enviar os dados do módulo
        # se o modulo não existir, criar um novo módulo
        # com o módulo criado, enviar dados



        return Response(status=status.HTTP_200_OK)