from rest_framework import serializers
#from django.contrib.auth.models import MyUser
from rest_framework.authtoken.models import Token
from .models import Panchayath,Person

from django.contrib.auth import get_user_model
User = get_user_model()

    
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("user_username","user_wanumber","user_panchayath","user_district")




class PanchayathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panchayath
        fields = ("id","user_panchayath","panchayath_population","panchayath_state","panchayath_district","panchayath_name")


class UserSerializer(serializers.ModelSerializer):
    
    person = PersonSerializer()

    class Meta:
        model = User
        fields = ['id','email','password','mobile_no',"person"]
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        person_data = validated_data.pop('person')

        user = User.objects.create_user(**validated_data)
        user.person = Person.objects.create(user=user, **person_data)
        Token.objects.create(user=user)
        return user