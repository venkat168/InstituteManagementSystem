from django.urls import path

from studentApp import views

urlpatterns=[
    path('',views.log_fun,name='log'),#it will display login.html page
    path('logdata',views.logdata_fun), #it will read the data and verify user is superuser and redirect to home.html page
    path('reg',views.reg_fun,name='reg'), #it will redirect to register.html page
    path('regdata',views.regdata_fun), #it will create superuser account
    path('home',views.home_fun,name='home'),#it willl redirect to home.html
    path('add_students',views.addstudents_fun,name='add'),#it will redirect to addstudent.html page
    path('readdata',views.readdata_fun),#it will insert records into studenttable
    path('display',views.display_fun,name='display'),
    path('update/<int:id>',views.update_fun,name='up'),
    path('delete/<int:id>',views.delete_fun,name='del'),
    path('log_out',views.log_out_fun,name='log_out')

]