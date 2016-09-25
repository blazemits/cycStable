from rest_framework import serializers
from accountManager.models import UserInformation

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInformation
        fields=('id','currentToken','emailID','password')
        #fields=('id','currentToken',)

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInformation
        fields=('id','currentToken')
        #fields='__all__'