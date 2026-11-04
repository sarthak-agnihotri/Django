
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    roll_number = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    semester = models.IntegerField()
    cgpa = models.FloatField()

# class Blogpost(models.Model):
#     title=models.CharField(max_length=50)
#     post=models.CharField(max_length=500,default="")
#     thumbnail=models.ImageField(upload_to='images/',null=True,blank=True)

#     def __str__(self):
#         return self.title
