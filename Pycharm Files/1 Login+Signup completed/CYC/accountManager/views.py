from django.shortcuts import render
from django.http import HttpResponse
from pip._vendor.distlib import database
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accountManager.serializers import SignUpSerializer,LoginSerializer
from usefulFunctions import tokenGenerator
from accountManager.models import UserInformation

@api_view(['POST'])
def tokenLoginFunction(request):
    token=request.data.get('token')
    if (token and UserInformation.objects.filter(currentToken=token).exists()): # if "token" contain some data
        dbObject=UserInformation.objects.get(currentToken=token)
        serializer = LoginSerializer(dbObject)
        userID=serializer.data.get('id')
        return  Response(data={"id":userID})
    else:
        return Response(data={"detail":"Token Not Matching,You Have to Login Again"})



@api_view(['POST'])
def usualLoginFunction(request):
    email=request.data.get('email')
    password=request.data.get('password')
    if (UserInformation.objects.filter(emailID=email,password=password).exists()):
        dbObject=UserInformation.objects.get(emailID=email)
        serializer=LoginSerializer(dbObject)
        userID=serializer.data.get('id')
        return  Response(data={"id":userID})
    else:
        return Response(data={"detail":"Email id or Password are not currect."})


@api_view(['POST'])
def signUpFunction(request):
    if request.method=='POST':
        serializer=SignUpSerializer(data=request.data)
        if serializer.is_valid():
            token=tokenGenerator(50)
            serializer.save(currentToken=token)
            return  Response(serializer.data)#data={"Sign-Up Athentification Portal"})
        else:
            return Response(data={"detail":"Incurrect Input Data"})
    else:
        return Response(data={"detail":"Request Method Not Allowed"},status=status.HTTP_400_BAD_REQUEST)

