from django.urls import path
from myapp import views
from django.contrib import admin  

urlpatterns = [
    path('', views.index, name='index'),  # 假设你有一个名为 index 的 view 函数
    path('listone/', views.listone, name='listone'),
    path('admin/', admin.site.urls), 
    path('listall/', views.listall, name='listall'),
]