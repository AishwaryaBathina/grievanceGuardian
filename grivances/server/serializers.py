from rest_framework import serializers
from .models import StudentModel, FacultyModel, ComplaintModel, UsersModel


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ('id','rno', 'password', 'name', 'email', 'mobile', 'year',  'section', 'branch', 'otp', 'isverified')


class UsersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ('username', 'password', 'accounttype')


class ComplaintModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintModel
        fields = ('id', 'studentid', 'complainttype', 'date', 'description', 'status')


class FacultyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyModel
        fields = ('username', 'password', 'name', 'email', 'mobile', 'branch', 'complainttype')
