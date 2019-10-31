from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from endpoints.models import Endpoint
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