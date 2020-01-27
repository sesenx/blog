"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from article import views                 #import index de views.py

urlpatterns = [
    path('admin/', admin.site.urls),                            #admin pannel
    path('',views.index,name="index"),                          #index.html , vers fonction index dans views.py
    path('about/',views.about,name="about"),                    #about.html , vers fonction about dans views.py
    path('detail/<int:id>', views.detail, name="detail"),       #variable id va etre integer,fonction detail dans views
    path('article/',include("article.urls")),   #si article/ path import le article/urls.py   (articles/)
    path('user/', include("user.urls")),        #si user/ path import le user/urls.py      (articles)

]


#a partir de navbar :  href="/article/dashboard/  , path /article/ envois vers article/url.py selon blog/urls.py
#dans url.py   path  dashboard/  views.dashboard  envois vers fichier  article/views.py fonction dashboard()
#avec attribue  dashboard
#dans article/views.py  le fonction dashboard est executé avec attribue dashboard
