from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .models import StudentModel, FacultyModel, ComplaintModel, UsersModel
from .serializers import StudentModelSerializer, FacultyModelSerializer, ComplaintModelSerializer, UsersModelSerializer
from rest_framework.views import APIView
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from .models import phoneModel
import base64


# Create your views here.
class UsersModelList(APIView):
    def get(self, request, format=None):
        user = UsersModel.objects.all()
        u_serializer = UsersModelSerializer(user, many=True)
        return Response(u_serializer.data)

    def post(self, request, format=None):
        u_serializer = UsersModelSerializer(data=request.data)
        if u_serializer.is_valid():
            u_serializer.save()
            return Response(u_serializer.data, status=status.HTTP_201_CREATED)
        return Response(u_serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UsersModelDetail(APIView):
    def get_user(self, pk):
        try:
            user = UsersModel.objects.get(pk=pk)
            return user
        except user.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_user(pk)
        u_serializer = UsersModelSerializer(user)
        return Response(u_serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_user(pk)
        u_serializer = UsersModelSerializer(user, request.data)
        if u_serializer.is_valid():
            u_serializer.save()
            return Response(u_serializer.data, status=status.HTTP_201_CREATED)
        return Response(u_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
class StudentModelList(APIView):
    def get(self, request, format=None):
        student = StudentModel.objects.all()
        s_serializer = StudentModelSerializer(student, many=True)
        return Response(s_serializer.data)

    def post(self, request, format=None):
        s_serializer = StudentModelSerializer(data=request.data)
        if s_serializer.is_valid():
            s_serializer.save()
            return Response(s_serializer.data, status=status.HTTP_201_CREATED)
        return Response(s_serializer.data, status=status.HTTP_400_BAD_REQUEST)


class StudentModelDetail(APIView):
    def get_student(self, pk):
        try:
            student = StudentModel.objects.get(pk=pk)
            return student
        except student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_student(pk)
        s_serializer = StudentModelSerializer(student)
        return Response(s_serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_student(pk)
        s_serializer = StudentModelSerializer(student, request.data)
        if s_serializer.is_valid():
            s_serializer.save()
            return Response(s_serializer.data, status=status.HTTP_201_CREATED)
        return Response(s_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_student(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Faculty.
class FacultyModelList(APIView):
    def get(self, request, format=None):
        faculty = FacultyModel.objects.all()
        f_serializer = FacultyModelSerializer(faculty, many=True)
        return Response(f_serializer.data)

    def post(self, request, format=None):
        f_serializer = FacultyModelSerializer(data=request.data)
        if f_serializer.is_valid():
            f_serializer.save()
            return Response(f_serializer.data, status=status.HTTP_201_CREATED)
        return Response(f_serializer.data, status=status.HTTP_400_BAD_REQUEST)


class FacultyModelDetail(APIView):
    def get_faculty(self, pk):
        try:
            faculty = FacultyModel.objects.get(pk=pk)
            return faculty
        except faculty.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        faculty = self.get_faculty(pk)
        f_serializer = FacultyModelSerializer(faculty)
        return Response(f_serializer.data)

    def put(self, request, pk, format=None):
        faculty = self.get_faculty(pk)
        f_serializer = FacultyModelSerializer(faculty, request.data)
        if f_serializer.is_valid():
            f_serializer.save()
            return Response(f_serializer.data, status=status.HTTP_201_CREATED)
        return Response(f_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        faculty = self.get_faculty(pk)
        faculty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Complaint.
class ComplaintModelList(APIView):
    def get(self, request, format=None):
        complaint = ComplaintModel.objects.all()
        print(complaint)
        c_serializer = ComplaintModelSerializer(complaint, many=True)
        return Response(c_serializer.data)

    def post(self, request, format=None):
        c_serializer = ComplaintModelSerializer(data=request.data)
        if c_serializer.is_valid():
            c_serializer.save()
            return Response(c_serializer.data, status=status.HTTP_201_CREATED)
        return Response(c_serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ComplaintModelDetail(APIView):
    def get_complaint(self, pk):
        try:
            complaint = ComplaintModel.objects.get(pk=pk)
            return complaint
        except complaint.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        complaint = self.get_complaint(pk)
        c_serializer = ComplaintModelSerializer(complaint)
        return Response(c_serializer.data)

    def put(self, request, pk, format=None):
        complaint = self.get_complaint(pk)
        c_serializer = ComplaintModelSerializer(complaint, request.data)
        if c_serializer.is_valid():
            c_serializer.save()
            return Response(c_serializer.data, status=status.HTTP_201_CREATED)
        return Response(c_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        complaint = self.get_complaint(pk)
        complaint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now()))


class getPhoneNumberRegistered(APIView):
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                Mobile=phone,
            )
            Mobile = phoneModel.objects.get(Mobile=phone)  # user Newly created Model
        Mobile.counter += 1  # Update Counter At every Call
        Mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(Mobile.counter))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"OTP": OTP.at(Mobile.counter)}, status=200)  # Just for demonstration

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong", status=400)    

