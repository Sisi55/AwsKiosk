from django.shortcuts import render
from django.http import HttpResponse
from .models import Name
from .order_decisiontree_recom import order_decisionTree_recom
from .item_collaborative_filtering import item_collaborativeFiltering


def itemCF(request, user_uuid):#사용자1, 아이템1
    
    result = item_collaborativeFiltering(user_uuid) #str:dict
    # dict으로 두 가지 종류 추천을 반환할거야
    # 아이템:안먹은 유사아이템
    # 사용자 > 안먹은 아이템  각각 하나씩
    #result = "{'user_cf':"+item_cf_result+",'items_sim':"+items_sim_dict+"}"
    return HttpResponse('<p>'+ result +'</p>') ## 마지막 str


def lambda_handler(request,humidity,temp,speed,emo1,emo2):#사용자1
    result_predict = order_decisionTree_recom(humidity,temp,speed,emo1,emo2)

    return HttpResponse('<p>'+ result_predict +'</p>')


def hello(request, name):
    return render(request, "hello.html", {"name": name})

    # return HttpResponse("<b>Hello " + name +"</b>")

def saveToDb(request, name):
    Name.objects.create(name = name)

    count = Name.objects.count()
    return HttpResponse("<h2>You have inserted a name successfully</h2> <br> count = " + str(count))


def index(request):
    return HttpResponse("<h2>You have reached the homepage</h2>")


def testsisi(request):
    return HttpResponse('<h1>장고 배포 성공</h1>')

