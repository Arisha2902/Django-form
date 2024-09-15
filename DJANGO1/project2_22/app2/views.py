from django.shortcuts import render,HttpResponse,redirect
from app2.models import *
from .form import Empforms

def home(request):
    # return HttpResponse("welcome")
    return render(request,"home.html")


def aboutus(variable):
    return render(variable,"aboutus.html")

def addEmp(req):
    return render(req,"newemp.html")

def Emp1(req):
    try:
        x= req.POST['e_nm']

        y= req.POST['e_id']
        z= req.POST['e_cont']
        e1=  Emp(emp_name=x,emp_id=y,emp_contact=z)
        e1.save()
        return redirect("showData")
    except Exception as e:
        return HttpResponse("something problematic")
    
def showEmp(req):
   data=Emp.objects.all()
   return render(req,"showEmp.html",{"data":data})

def deletedata(req):
    try:
        eid=req.GET['eid']
        data= Emp.objects.get(id=eid)
        data.delete()
        return redirect("showData")
        # return HttpResponse("Record Deleted")
    except Exception as e:
        return HttpResponse(e)

def updatedata(req):
    try:
       eid=req.GET['eid']
       e1= Emp.objects.get(id=eid)
       return render(req,"updatedata.html",{'e1':e1})
    except Exception as e:
        return HttpResponse(e)

# def updatedata2(req):
#     try:
#         x= req.POST['emp_name']
#         y= req.POST['emp_id']
#         z= req.POST['e_cont']
#         d= req.POST['eid']
#         e1= Emp.objects.get(id=d)
#         e1.emp_name=x
#         e1.emp_id=y
#         e1.emp_contact=z
#         e1.save()
#         return redirect("showEmp")
#     except Exception as e:
#         return HttpResponse(e)
# Create your views here.

def form_Emp(req):
    if req.method == "POST":
      sfrm = Empforms(req.POST)
      if sfrm.is_valid():
            x=sfrm.cleaned_data['Name']
            y=sfrm.cleaned_data['Age']
            Sobj=Emp(emp_name=x,emp_id=y)
            Sobj.save()
            return redirect('showallstudent') 
    else:
        SS=Empforms()
        return render(req,"formEmp.html",{"Emp1":SS})
    
def showAllStudent(req):
    SS=Emp.objects.all()
    return render(req,"allstudent.html",{"Skey":SS})





