from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User, Teacher, Student, AI


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_student', 'is_teacher', 'is_ai')
        extra_kwargs = {'password': {'write_only': True}}


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class AISerializer(serializers.ModelSerializer):
    class Meta:
        model = AI
        fields = '__all__'


class TeacherRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Teacher
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}, 'username': {'write_only': True}}

    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create_user(username=validated_data['user']['username'],
                                        email=validated_data['email'],
                                        password=validated_data['user']['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        is_teacher=True
                                        )

        # Add new variables here
        teacher = Teacher.objects.create(
            user=user,
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address']
        )
        return teacher


class TeacherLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        fields = '__all__'
        extra_kwargs = {'is_teacher': {'required': False},
                        'is_student': {'required': False},
                        'is_ai': {'required': False}}

    def validate(self, data):
        teacher = authenticate(**data)
        if teacher and teacher.is_active:
            return teacher
        raise serializers.ValidationError('Invalid Credentials.')


class StudentRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}, 'username': {'write_only': True}}

    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create_user(username=validated_data['user']['username'],
                                        email=validated_data['email'],
                                        password=validated_data['user']['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        is_student=True)

        student = Student.objects.create(
            user=user,
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address']
        )
        return student


class StudentLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        fields = '__all__'
        extra_kwargs = {'is_teacher': {'required': False},
                        'is_student': {'required': False},
                        'is_ai': {'required': False}}

    def validate(self, data):
        student = authenticate(**data)
        if student and student.is_active:
            return student
        raise serializers.ValidationError('Invalid Credentials.')


class AIRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = AI
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}, 'username': {'write_only': True}}

    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create_user(username=validated_data['user']['username'],
                                        email=validated_data['email'],
                                        password=validated_data['user']['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        is_ai=True)

        ai = AI.objects.create(
            user=user,
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address']
        )
        return ai


class AILoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        fields = '__all__'
        extra_kwargs = {'is_teacher': {'required': False},
                        'is_student': {'required': False},
                        'is_ai': {'required': False}}

    def validate(self, data):
        ai = authenticate(**data)
        if ai and ai.is_active:
            return ai
        raise serializers.ValidationError('Invalid Credentials.')
