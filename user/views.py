from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer, UserLoginSerializer, UserCreatedSerializer, UserDepositSerializer
from .models import User
from .serializers import UserSerializer
from . import helpers
import re
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
        "User SignUp": "api/user/signup/",
        "User Deposit": "api/user/deposit/",
        "Users Withdrawal": 'api/user/withdrawal/',
        "Users Account Details": 'api/user/accountdetails/',

    }
    return Response(list)


@api_view(['POST'])
def userCreate(request):
    # return Response({"Status":"Coming Soon"})
    try:
        request.data['firstname'] = request.data['firstname'].lower()
        request.data['lastname'] = request.data['lastname'].lower()
        request.data['username'] = request.data['username'].lower()
        password = request.data['password']
        request.data['balance'] = float(0)
        request.data['accountnumber'] = helpers.generate_account_number()
        uname = str(request.data['username'])
        uniqueUsernameStatus = helpers.checkUsernameInput(uname)
        serializer = UserSerializer(data=request.data)

        if uniqueUsernameStatus == True:
            try:
                if serializer.is_valid():
                    serializer.save()
                    user = User.objects.all().last()
                    serializer = UserCreatedSerializer(user)

                    response = {
                    "Status": "200",
                    "data": [
                        serializer.data
                    ]
                    }
            except:
                response = {
                    "Error: User Not Created : Check Input"
                }
    
        elif uniqueUsernameStatus == False:
            response = {
                "Error: Username Already Exists"
            }       

    except Exception as e:
        response = {
            "Error Occured": str(e)
        }

    return Response(response)


@api_view(['GET'])
def accountdetails(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated')

    try:

        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthorized')

    user = User.objects.filter(id=payload['id']).first()
    # user = User.objects.get(id=payload['id'])
    serializer = UserCreatedSerializer(user)

    return Response(serializer.data)
    # return Response(token)


@api_view(['POST'])
def deposit(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated')

    try:

        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        user = User.objects.get(id=payload["id"])
        if (float(request.data['amount']) > 0):
            current_balance = user.balance
            new_balance = current_balance + float(request.data['amount'])
            user.balance = new_balance

            user.save()
            response = {
                "status": 200,
                "message": "Deposit Successful"
            }
        else:
            response = {

                "status": 400,
                "message": "Invalid Amount "
            }

    except KeyError:
        response = {
            "status": 400,
            "message": "Missing Amount"
        }
    except ValueError:
        response = {
            "status": 400,
            "message": "Invalid Amount"
        }

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthorized')

    # users = User.objects.get(id=pk)
    return Response(response)


@api_view(['POST'])
def withdrawal(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated')

    try:

        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        user = User.objects.get(id=payload["id"])
        current_balance = user.balance
        if (current_balance >= float(request.data['amount'])):
            new_balance = current_balance - float(request.data['amount'])
            user.balance = new_balance

            user.save()
            response = {
                "status": "200",
                "message": "Withdrawal Successful"
            }
        else:
            response = {
                "status": "400",
                "message": "Insufficient Funds"
            }

    except KeyError:
        response = {
            "status": "400",
            "message": "Missing Amount"
        }
    except ValueError:
        response = {
            "status": "400",
            "message": "Invalid Amount"
        }

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthorized')

    # users = User.objects.get(id=pk)
    return Response(response)
