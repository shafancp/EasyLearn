from django.db import models

# Create your models her
class Login(models.Model):
    username=models.CharField(max_length=100,default="")
    password=models.CharField(max_length=100,default="")
    type = models.CharField(max_length=100, default="")
class Subject(models.Model):
    name= models.CharField(max_length=100, default="")

class Tutor(models.Model):
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    photo = models.CharField (max_length=500, default="")
    idproof = models.CharField(max_length=500, default="")
    DOB = models.DateField()
    gender = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    phoneno = models.CharField(max_length=100, default="")
    houseno = models.CharField(max_length=100, default="")
    place = models.CharField(max_length=100, default="")
    district = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    PIN = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="")
    qualification = models.CharField(max_length=100, default="")
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    SUBJECT = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Student(models.Model):
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    DOB = models.DateField()
    gender = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    phoneno = models.CharField(max_length=100, default="")
    photo = models.CharField(max_length=500, default="")
    course = models.CharField(max_length=100, default="")
    institution = models.CharField(max_length=100, default="")
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)

class Notes(models.Model):
    topic = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=100, default="")
    date = models.DateField()
    note = models.CharField(max_length=500, default="")
    TUTOR= models.ForeignKey(Tutor, on_delete=models.CASCADE)

class Doubts(models.Model):
    doubt= models.CharField(max_length=100, default="")
    reply = models.CharField(max_length=100, default="")
    date = models.DateField()
    status = models.CharField(max_length=100, default="")
    NOTE = models.ForeignKey(Notes, on_delete=models.CASCADE)
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)

class Complaint(models.Model):
    head = models.CharField(max_length=100, default="")
    complaint = models.CharField(max_length=100, default="")
    reply = models.CharField(max_length=100, default="")
    date = models.DateField()
    status = models.CharField(max_length=100, default="")
    FROM = models.ForeignKey(Login, on_delete=models.CASCADE, default="")

class Feedback(models.Model):
    feedback = models.CharField(max_length=100, default="")
    type = models.CharField(max_length=100, default="")
    date = models.DateField()
    FROM = models.ForeignKey(Login, on_delete=models.CASCADE, default="")










