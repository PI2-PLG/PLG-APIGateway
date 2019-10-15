from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import CustomUser
from users.serializers import CustomUserSerializer
import io


class NewUserView(APIView):

    def post(self, request):
        try:
            name = request.data['name']
            email = request.data['email']
            username = request.data['username']
            password = request.data['password']

            new_user = CustomUser()
            new_user.name = name
            new_user.email = email
            new_user.username = username
            new_user.set_password(password)
            new_user.save()

            response = "{response: user_successfully_created}"
            return Response(response, status=status.HTTP_201_CREATED)
        except:
            response = "{response: user_unseccessfully_created}"
            return Response(response, status=status.HTTP_200_OK)


class AddNotificatioTokenView(APIView):

    def post(self, request):
        try:
            username = request.data['username']
            user = CustomUser.objects.get(username=username)
        except:
            response = "{response: user_not_found}"
            return Response(response, status=status.HTTP_200_OK)

        try:
            username = request.data['username']
            notification_token = request.data['notification_token']
            user.notification_token = notification_token
            user.save()
            response = "{response: token_successfully_added}"
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = "{response: user_unseccessfully_added}"
            return Response(response, status=status.HTTP_200_OK)


class UpdateUserView(APIView):

    def post(self, request):
        try:
            username = request.data['username']
            user = CustomUser.objects.get(username=username)
            response = CustomUserSerializer(user)
            print(response.data)
            return Response(response.data, status=status.HTTP_200_OK)
        except:
            response = "{response: user_not_found}"
            return Response(response, status=status.HTTP_200_OK)
