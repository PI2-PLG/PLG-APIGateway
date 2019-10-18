from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
import io


class NewUser(APIView):

    def post(self, request):
        try:
            data = request.data['user']
            token = request.data['token']
            username = data['username']
            email = data['email']
            name = data['name']
            password = data['password']
            notification_token = token['notification_token']
            new_user = CustomUser()
            new_user.name = name
            new_user.email = email
            new_user.username = username
            new_user.set_password(password)
            new_user.notification_token = notification_token
            new_user.save()
            response = "{response: user_successfully_created}"
            return Response(response, status=status.HTTP_201_CREATED)
        except:
            response = "{response: user_unseccessfully_created}"
            return Response(response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


class UserLogin(APIView):

    def post(self, request):
        try:
            username = request.data["username"]
            password = request.data["password"]

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    response = CustomUserSerializer(user)
                    return Response(response.data, status=status.HTTP_200_OK)
                else:
                    response = "{response:accont_disabled}"
                    return Response(response, status=status.HTTP_200_OK)
            else:
                    response = "{response:invalid_login}"
                    return Response(response, status=status.HTTP_200_OK)

        except:
            response = "{response:invalid_login}"
            return Response(response, status=status.HTTP_200_OK)


class GetUserData(APIView):

    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated,)

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
