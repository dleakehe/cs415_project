from rest_framework import serializers
from cs415.models import Characters, Classskills, Classes, Raceskills, Races, User

class CharactersSerializer(serializers.ModelSerializer):
    class Meta:
            model = Characters
            fields = '__all__'

class ClassskillsSerializer(serializers.ModelSerializer):
    class Meta:
            model = Classskills
            fields = '__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
            model = Classes
            fields = '__all__'

class RaceskillsSerializer(serializers.ModelSerializer):
    class Meta:
            model = Raceskills
            fields = '__all__'  

class RacesSerializer(serializers.ModelSerializer):
    class Meta:
            model = Races
            fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = '__all__'