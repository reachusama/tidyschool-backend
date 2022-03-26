from django.contrib import auth
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import TeacherRegisterSerializer, TeacherLoginSerializer, TeacherSerializer, UserSerializer, \
    StudentRegisterSerializer, StudentLoginSerializer, StudentSerializer, AIRegisterSerializer, AILoginSerializer, \
    AISerializer
from .models import Teacher, Student, AI


class TeacherSignUpAPI(generics.GenericAPIView):
    serializer_class = TeacherRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        teacher_data = TeacherSerializer(teacher, context=self.get_serializer_context()).data
        token = AuthToken.objects.create(teacher.user)

        return Response({
            "teacher": teacher_data,
            "username": teacher.user.username,
            "token": token[1]
        })


class TeacherSignInAPI(generics.GenericAPIView):
    serializer_class = TeacherLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        user_data = UserSerializer(user, context=self.get_serializer_context()).data

        teacher = Teacher.objects.get(user__id=user_data["id"])
        teacher_data = TeacherSerializer(teacher).data

        token = AuthToken.objects.create(user)
        return Response({
            "teacher": teacher_data,
            "username": user.username,
            "token": token[1]
        })


class TeacherMainUser(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class StudentSignUpAPI(generics.GenericAPIView):
    serializer_class = StudentRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        student_data = StudentSerializer(student, context=self.get_serializer_context()).data
        token = AuthToken.objects.create(student.user)
        return Response({
            "student": student_data,
            "username": student.user.username,
            "token": token[1]
        })


class StudentSignInAPI(generics.GenericAPIView):
    serializer_class = StudentLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        user_data = UserSerializer(user, context=self.get_serializer_context()).data

        student = Student.objects.get(user__id=user_data["id"])
        student_data = StudentSerializer(student).data

        token = AuthToken.objects.create(user)

        return Response({
            "student": student_data,
            "username": student.user.username,
            "token": token[1]
        })


class StudentMainUser(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class AISignUpAPI(generics.GenericAPIView):
    serializer_class = AIRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ai = serializer.save()
        ai_data = AISerializer(ai, context=self.get_serializer_context()).data
        token = AuthToken.objects.create(ai.user)
        return Response({
            "ai": ai_data,
            "username": ai.user.username,
            "token": token[1]
        })


class AISignInAPI(generics.GenericAPIView):
    serializer_class = AILoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        user_data = UserSerializer(user, context=self.get_serializer_context()).data

        ai = AI.objects.get(user__id=user_data["id"])
        ai_data = AISerializer(ai).data

        token = AuthToken.objects.create(user)

        return Response({
            "ai": ai_data,
            "username": ai.user.username,
            "token": token[1]
        })


class AIMainUser(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
