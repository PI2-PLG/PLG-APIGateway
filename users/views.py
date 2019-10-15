from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import CustomUser
import io

@api_view(['POST'])
def new_user(request):
    # print(request.data['name'])
    # print(request.data['email'])
    # print(request.data['username'])
    # print(request.data['password'])
    try:
        if request.method == 'POST':
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

@api_view(['POST'])
def add_notification_token(request):
    print(request.data['username'])
    print(request.data['notification_token'])

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