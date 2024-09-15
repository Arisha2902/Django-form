from django.urls import path
from . import views

urlpatterns=[
    path('home', views.home,name="home"),
    path('aboutus', views.aboutus,name="about"),
    path('',views.Emp1,name="addData"),
    path('newEmp',views.addEmp,name="newEmp"),
    path('showData',views.showEmp,name="showData"),
    path('deleteData',views.deletedata,name="deleteData"),
    path('updateData',views.updatedata,name="updateData"),
    # path('updatedata2',views.updatedata2,name="updatedata2")
    path('addnew1',views.form_Emp,name="formEmp"),
    path('',views.showAllStudent,name="showallstudent")
]

