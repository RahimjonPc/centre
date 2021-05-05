from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import settings
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, AllowAny


from users.models import LeaderProfile, Teacher, Student, StudentGroup
from events.models import Events
from cources.models import Courses
from .serializers import LeaderSerializer, TeacherListSerializer, StudentListSerializer, TeacherCreateSerializer, StudentCreateSerializer, StudentGroupListSerializer, StudentGroupCreateSerializer, MyTokenObtainPairSerializer
from .permissions import StudentUpdatePermission, TeacherUpdatePermissionClass, TeacherListPermission

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class LeaderView(generics.ListAPIView):
    queryset = LeaderProfile
    serializer_class = LeaderSerializer
    permission_class = [IsAuthenticated]


class TeachersListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    permission_classes = [TeacherListPermission, IsAuthenticated]



class TeacherCreateView(generics.CreateAPIView):
    permission_class = [AllowAny]
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer
    


class TeacherPasswordUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer
    permission_classes = [TeacherUpdatePermissionClass, IsAuthenticated]


class TeacherUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer
    permission_classes = [AllowAny]


class TeacherAccountView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher
    serializer_class = TeacherListSerializer


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [IsAuthenticated]

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [AllowAny]


class StudentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [AllowAny]


class StudentAccountView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    permission_classes = StudentListSerializer

  

class StudentGroupListView(generics.ListAPIView):
    serializer_class = StudentGroupListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        groups = StudentGroup.objects.all()
        if self.request.GET.get('teacher_of_group'):
            teacher = self.request.GET.get('teacher_of_group')
            return Student.objects.filter(StudentGroup__teacher=teacher).distinct()
        else:
            return StudentGroup.objects.all()


class StudentGroupCreateView(generics.CreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupCreateSerializer
    permission_classes = [IsAuthenticated]



class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
