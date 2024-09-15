from django.shortcuts import render
from django.http import HttpResponse
import datetime
from app1.models import Student
from app1.models import Course



def home(request):
    dateobj= datetime.datetime.now()
    # return HttpResponse("welcome")
    return render(request,"home.html",{"date":dateobj})

def aboutus(variable):
    # dateobj= datetime.datetime.now()
        # context  ={
    #    ' heading': "django tutorial", 
    #    'content': "this is best"
    # }
    # return HttpResponse("this is about us")
    return render(variable,"aboutus.html")

def contactus(request3):
    return render(request3,"aboutus.html")

def attendStudent(res):
    try:
        s1= Student( stu_name="fg",stu_branch="hddj",stu_contact=23245)
        # s1= Student(455,"hddj",23245)
        s1.save()
        return HttpResponse("data saved")
    except Exception as e:
        return HttpResponse(f"something problematic: {str(e)}")

    #     return HttpResponse("something problematic")
 
# def Emp1(res2):
#     try:
#         e1=  Emp1("abc",1234)
#         e1.save()
#         return HttpResponse("data saved")
#     except Exception as e:
#         return HttpResponse(f"something problematic: {str(e)}")

def course(res):
    try:
        c=course(c_id=25)
        c.save()
        return HttpResponse("data saved")
    except:
        return HttpResponse("something problematic")




# Create your views here.
