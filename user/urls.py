from django.contrib import admin
from django.urls import path
from . import views                                     #import views.py du repertoire actuel
from django.conf import settings
from django.conf.urls.static import static

app_name="user"


urlpatterns=[
    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#a partir de navbar :  href="/article/dashboard/  , path /article/ envois vers article/url.py selon blog/urls.py
#dans url.py   path  dashboard/  views.dashboard  envois vers fichier  article/views.py fonction dashboard()
#avec attribue  dashboard
#dans article/views.py  le fonction dashboard est executé avec attribue dashboard