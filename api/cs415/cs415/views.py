from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Characters, Classskills, Classes, Raceskills, Races
from cs415.serializers import UserSerializer, CharactersSerializer, ClassskillsSerializer, ClassesSerializer, RaceskillsSerializer, RacesSerializer
from cs415.settings import JWT_AUTH
from cs415.authentication import JWTAuthentication
import datetime

class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({'success': False, 'error': 'Email and Password must have a value'}, status = status.HTTP_400_BAD_REQUEST)

        check_user = User.objects.filter(email=email).exists()
        if check_user == False:
            return Response({'success': False, 'error': 'User with this email does not exist'}, status = status.HTTP_404_NOT_FOUND)
        
        check_pass = User.objects.filter(email = email, pass_field = password).exists()
        if check_pass == False:
            return Response({'success': False, 'error': 'Incorrect Password'}, status = status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(email =  email, pass_field = password)
        serializer = UserSerializer(user, data={'last_login': str(datetime.datetime.now())},  partial = True)
        if serializer.is_valid():
            serializer.save()
            
        if  user is not None:
            jwt_token = JWTAuthentication.create_jwt(user)
            data = {
                'token': jwt_token
            }
            return Response({'success': True,
                             'token': jwt_token,
                             'user_id': user.user_id},
                             status=status.HTTP_200_OK)
        else:
            return Response({'success': False,
                             'error': 'Invalid Login Credentials'},
                             status=status.HTTP_400_)

        
    
class GetSingleUserAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user_data = {}
        user = User.objects.get(pk=id)
        user_serializer = UserSerializer(user)
        user_data.update({"user": user_serializer.data})
        characters = CharactersSerializer(Characters.objects.filter(user_id=user.user_id), many=True)
        user_data.update({"characters": characters.data})
        return Response(user_data)

class CharactersAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        characters = Characters.objects.all()
        serializer = CharactersSerializer(characters, many=True)
        return Response({'characters': serializer.data})

class GetSingleCharacterAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = Characters.objects.get(pk=id)
        serializer = CharactersSerializer(user)
        return Response({'characrter': serializer.data})
    
class ClassskillsAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        cskills = Classskills.objects.all()
        serializer = ClassskillsSerializer(cskills, many=True)
        return Response({'classSkills': serializer.data})
    
class GetSingleClassSkillAPIView(APIView):
    def get(self,request,skillname):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        cskill = Classskills.objects.get(skill=skillname)
        serializer = ClassskillsSerializer(cskill)
        return Response({'classskill': serializer.data})
    
class ClassesAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response({'classes': serializer.data})
    
class GetSingleClassAPIView(APIView):
    def get(self,request,job):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        cclass = Classes.objects.get(classname=job)
        serializer = ClassesSerializer(cclass)
        return Response({'job': serializer.data})
    
class RaceSkillsAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        rskills = Raceskills.objects.all()
        serializer = RaceskillsSerializer(rskills, many=True)
        return Response({'raceSkills': serializer.data})
    
class GetSingleRaceSkillAPIView(APIView):
    def get(self,request,skillname):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        rskill = Raceskills.objects.get(skill=skillname)
        serializer = RaceskillsSerializer(rskill)
        return Response({'raceskill': serializer.data})
    
class RacesAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        races = Races.objects.all()
        serializer = RacesSerializer(races, many=True)
        return Response({'races': serializer.data})
    
class GetSingleRaceAPIView(APIView):
    def get(self,request,races):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        race = Races.objects.get(racename=races)
        serializer = RacesSerializer(race)
        return Response({'race': serializer.data})