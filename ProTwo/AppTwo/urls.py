from django.conf.urls import include
from django.urls import path
from AppTwo import views

urlpatterns = [
    path('index',views.index,name = 'index'),
]