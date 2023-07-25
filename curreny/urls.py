from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from curreny import views as padmin
from user import views as usr
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',padmin.index,name='index'),
    path('home/', padmin.home, name='home'),
    path('userlogin/',padmin.userlogin, name='userlogin'),
    path('adminlogin/', padmin.adminlogin, name='adminlogin'),
    path('padminentered/', padmin.padminentered, name='padminentered'),
    path('userview/', padmin.userview, name='userview'),
    path('adminlogout/', padmin.adminlogout,name='adminlogout'),

    path('userregister/', usr.userregister, name='userregister'),
    path('usersignup/',usr.usersignup, name='usersignup'),
    path('userloginaction/',usr.userloginaction, name='userloginaction'),
    path('userlogout/', usr.userlogout, name='userlogout'),
    path('userpredict/', usr.userpredict,name='userpredict'),
    path('userhome/',usr.userhome,name='userhome'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)