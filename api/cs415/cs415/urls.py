"""
URL configuration for cs415 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cs415 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Login.as_view()),
    path('users/', views.UserAPIView.as_view()),
    path('users/user/<int:id>', views.GetSingleUserAPIView.as_view()),
    path('classskills/', views.ClassskillsAPIView.as_view()),
    path('classskills/classskill/<str:skillname>', views.GetSingleClassSkillAPIView.as_view()),
    path('classes/', views.ClassesAPIView.as_view()),
    path('classes/class/<str:job>', views.GetSingleClassAPIView.as_view()),
    path('raceskills/', views.RaceSkillsAPIView.as_view()),
    path('raceskills/raceskill/<str:skillname>', views.GetSingleRaceSkillAPIView.as_view()),
    path('races/', views.RacesAPIView.as_view()),
    path('races/race/<str:races>', views.GetSingleRaceAPIView.as_view()),
    path('characters/', views.CharactersAPIView.as_view()),
    path('characters/character/<int:id>', views.GetSingleCharacterAPIView.as_view()),
]
