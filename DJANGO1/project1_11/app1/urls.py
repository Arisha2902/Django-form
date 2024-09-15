from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('aboutus',views.aboutus),
    path('contactus',views.contactus),
    path('student',views.attendStudent),
    path('Cou',views.Course)
 ]
