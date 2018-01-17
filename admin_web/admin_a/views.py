from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from admin_a import models
# Create your views here.


def index(request):
    name = models.UserInfo.objects.all()
    request.user_name = "haha"
    return render(request,'index.html',{'name':name})