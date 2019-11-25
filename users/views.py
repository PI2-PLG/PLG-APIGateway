from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny
import io


class NewUser(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            data = request.data['user']
            token = request.data['token']
            username = data['username']
            email = data['email']
            name = data['name']
            password = data['password']
            notification_token = token['notification_token']
            print(f'======================\n[LOG] Creating a new user:\nUsername: {username}\nEmail: {email}\nNotification_Token: {notification_token}\n======================\n')
            new_user = CustomUser()
            new_user.name = name
            new_user.email = email
            new_user.username = username
            new_user.set_password(password)
            new_user.notification_token = notification_token
            new_user.save()
            # response = "{response: user_successfully_created}"
            return Response({'response': 'user_successfully_created'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'response': 'user_unseccessfully_created'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


class UserLogin(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        try:

            data = request.data['user']
            username = data["username"]
            password = data["password"]

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    response = CustomUserSerializer(user)
                    username = response.data['username']
                    email = response.data['email']
                    name = response.data['name']
                    notification_token = response.data['notification_token']

                    return Response(
                        {
                            'username': username,
                            'email': email,
                            'name': name,
                            'notification_token': notification_token,
                            'response': 'successfully_login'
                        },
                        status=status.HTTP_200_OK)
                else:
                    return Response({'response': 'accont_disabled'}, status=status.HTTP_200_OK)
            else:
                return Response({'response': 'invalid_login'}, status=status.HTTP_200_OK)

        except:
            return Response({'response': 'unable_to_process'}, status=status.HTTP_200_OK)


class GetUserData(APIView):

    permission_classes = (AllowAny,)

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

class AllTokens(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        users = CustomUser.objects.all()
        tokens = []
        for user in users:
            tokens.append(user.notification_token)

        response = {}
        response["token_list"] = tokens

        return Response(response, status=status.HTTP_200_OK)