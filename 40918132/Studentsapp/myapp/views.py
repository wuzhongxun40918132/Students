from django.shortcuts import render
from .models import Student  # 假设你的学生模型叫做 Student

def index(request):
    # 处理首页逻辑
    students = Student.objects.all()  # 获取所有学生数据
    return render(request, 'index.html', {'students': students})

def listone(request):
    # 获取单个学生数据
    student = Student.objects.get(cName="李采茜")  # 假设你的模型是 Student，你可能需要更改为符合你的模型设置
    return render(request, 'listone.html', {'student': student})

def listall(request):
    # 处理列表所有学生的逻辑
    students = Student.objects.all()  # 获取所有学生信息，你可能需要自定义这个查询以匹配你的模型
    return render(request, 'listall.html', {'students': students})