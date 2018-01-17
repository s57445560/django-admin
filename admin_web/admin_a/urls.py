from django.conf.urls import url
from django.contrib import admin

from admin_a import views


urlpatterns = [
    url(r'index/', views.index, name="sunyang"),
]