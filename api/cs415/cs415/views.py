from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Characters, Classskills, Classes, Raceskills, Races
from cs415.serializers import UserSerializer, CharactersSerializer, ClassskillsSerializer, ClassesSerializer, RaceskillsSerializer, RacesSerializer

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
    
class GetSingleUserAPIView(APIView):
    def get(self,request,id):
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user)
        return Response({'user': serializer.data})

class CharactersAPIView(APIView):
    def get(self,request):
        characters = Characters.objects.all()
        serializer = CharactersSerializer(characters, many=True)
        return Response({'characters': serializer.data})

class GetSingleCharacterAPIView(APIView):
    def get(self,request,id):
        user = Characters.objects.get(pk=id)
        serializer = CharactersSerializer(user)
        return Response({'characrter': serializer.data})
    
class ClassskillsAPIView(APIView):
    def get(self,request):
        cskills = Classskills.objects.all()
        serializer = ClassskillsSerializer(cskills, many=True)
        return Response({'classSkills': serializer.data})
    
class GetSingleClassSkillAPIView(APIView):
    def get(self,request,skillname):
        cskill = Classskills.objects.get(skill=skillname)
        serializer = ClassskillsSerializer(cskill)
        return Response({'classskill': serializer.data})
    
class ClassesAPIView(APIView):
    def get(self,request):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response({'classes': serializer.data})
    
class GetSingleClassAPIView(APIView):
    def get(self,request,job):
        cclass = Classes.objects.get(classname=job)
        serializer = ClassesSerializer(cclass)
        return Response({'job': serializer.data})
    
class RaceSkillsAPIView(APIView):
    def get(self,request):
        rskills = Raceskills.objects.all()
        serializer = RaceskillsSerializer(rskills, many=True)
        return Response({'raceSkills': serializer.data})
    
class GetSingleRaceSkillAPIView(APIView):
    def get(self,request,skillname):
        rskill = Raceskills.objects.get(skill=skillname)
        serializer = RaceskillsSerializer(rskill)
        return Response({'raceskill': serializer.data})
    
class RacesAPIView(APIView):
    def get(self,request):
        races = Races.objects.all()
        serializer = RacesSerializer(races, many=True)
        return Response({'races': serializer.data})
    
class GetSingleRaceAPIView(APIView):
    def get(self,request,races):
        race = Races.objects.get(racename=races)
        serializer = RacesSerializer(race)
        return Response({'race': serializer.data})