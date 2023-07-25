from django.shortcuts import render
from django.contrib import messages
from user.models import *

def index(request):
    return render(request, "index.html")

def userlogin(request):
    return render(request, 'user/userlogin.html')

def adminlogin(request):
    return render(request, 'admin/adminlogin.html')

def home(request):
    return render(request, 'index.html')

def padminentered(request):
    if request.method == 'POST':
        uname = request.POST['adminname']
        passwd = request.POST['adminpasswd']
        if uname == 'admin' and passwd == 'admin':
            return render(request, "admin/padminentered.html")
        else:
            messages.success(request,"invalied Credentials")
            return render(request, "admin/adminlogin.html")
    return render(request, "padminentered.html")

def userview(request):
    data_list = UserModel.objects.all()
    return render(request, "admin/userview.html", {'data': data_list})

def adminlogout(request):
    return render(request, "admin/adminlogin.html")