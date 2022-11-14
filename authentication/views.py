import datetime
import jwt
import json
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from django.shortcuts import render
from urllib import response
import re
from user.models import User
from user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from ..api.serializers import UserSerializer, UserLoginSerializer, UserCreatedSerializer, UserDepositSerializer
# from ..api.models import User
# from ..api.serializers import UserSerializer
# from ..api import helpers
# from ..api.serializers import UserSerializer
import sys
sys.path.append("..")
# import api.serializers.UserSerializer


# Create your views here.


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        "status": 200,
        'Message': 'Logout Successful'
    }
    return response


@api_view(['POST'])
def userLogin(request):
    response = Response()
    try:
        print("i am here 0")
        username_input = request.data['username'].lower()
        password_input = request.data['password']
        # user = User.objects.filter(username=username_input).first()
        print("i am here 0.5")
        user = User.objects.filter(username=username_input).first()
        print("i am here 0.9")
        # user_serializer = UserSerializer(user, many=False)
        
        print("i am here1")
        if user is None:
            raise AuthenticationFailed("User not Found!")

        if not user.check_password(password_input):
            raise AuthenticationFailed("Incorrect Password!")

        print("i am here2")
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
            "is_superuser": user.is_superuser,

        }
        
        print("i am here3")
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        print("i am here4")
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            "Message": "Login Successful",
            "Status": 200,
            'jwt': token
        }

    except Exception as e:  # work on python 2.x
        response.data = {
            "Error Occured": str(e)
        }
        
   
    return response
