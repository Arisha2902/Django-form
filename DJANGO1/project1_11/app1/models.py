from django.db import models

class Student(models.Model):
    stu_name=models.CharField(max_length=30)
    stu_branch=models.CharField(max_length=30)
    stu_contact=models.IntegerField()

class Course(models.Model):
    c_id=models.IntegerField()

class Emp1(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_contact=models.IntegerField()