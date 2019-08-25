"""TestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from .views import hello, index, saveToDb, testsisi,lambda_handler, itemCF

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_recom/<humidity>/<temp>/<speed>/<emo1>/<emo2>', lambda_handler), #humidity,temp,speed,emotion
    
    path('hello/<name>', hello),
    path('savetodb/<name>', saveToDb),
    path('item_cf/<user_uuid>', itemCF), #userid말고 uuid를 주겠지 함수에서 변경해야 한다
    path('testsisi/', testsisi),
    path('', index) # 이게 기본url? 어쨌든 이 아래에 path()있으면 nginx에서 인식안된다 시발
    
]
