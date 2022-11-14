from rest_framework.response import Response
from rest_framework.decorators import api_view


from urllib import response
from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
import json
import jwt
import datetime



@api_view(['GET'])
def apiOverview(request):
    list = {
        "User SignUp": "/api/user/signup/",
        "User Deposit": "/api/user/deposit/",
        "Users Withdrawal": '/api/user/withdrawal/',
        "Users Account Details": '/api/user/accountdetails/',
        "User LogIn": '/api/authentication/login/',
        "User LogOut": '/api/authentication/logout/',
       

    }
    return Response(list)


 
        
