from django.db import models
from django.db.models import Model


class UsersModel(Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    accounttype = models.CharField(max_length=50)
    def __str__(self):
            return str(self.username)

class StudentModel (Model):
    rno = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    otp = models.CharField(max_length=50, blank=True, null=True)
    isverified = models.CharField(max_length=50, null=True, blank=True, default=False)
    def __str__(self):
            return str(self.name)

class ComplaintModel(Model):
    studentid = models.CharField(max_length=50)
    complainttype = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    def __str__(self):
            return str(self.description)


class FacultyModel(Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    complainttype = models.CharField(max_length=50)
    def __str__(self):
            return str(self.username)

class phoneModel(models.Model):
    Mobile = models.CharField(max_length=50)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    def __str__(self):
            return str(self.Mobile)