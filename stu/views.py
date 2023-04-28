import json
import os

from PIL.Image import Image

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from stu import models


# Create your views here.

def index(request):
    return HttpResponse('hello world!')


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def user_detail(request):
    queryset = models.UserInfo2.objects.all()
    for obj in queryset:
        print(obj.id, obj.name, obj.phone, obj.CustomerID, obj.email, obj.address, obj.industry)

    return render(request, "user_detail.html", {'queryset': queryset})
def add_client(request):
    """tianjiabuim"""

    if request.method == "GET":
        return render(request, "change_form_add.html")

    name = request.POST.get("name")
    phone = request.POST.get("phone")
    CustomerID = request.POST.get("CustomerID")
    email = request.POST.get("email")
    address = request.POST.get("address")
    industry = request.POST.get("industry")
    models.UserInfo2.objects.create(name=name, phone=phone, CustomerID=CustomerID, email=email, address=address,
                                    industry=industry)
    # 跳转
    if request.method == "POST":

     return redirect("/user_detail/")

def create_users(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        project_name = data.get('project_name')
        project_author = data.get('project_author')
        project_type=data.get(' project_type')
        project_SingleDetermination=data.get('Project_SingleDetermination')
        folder_name = f"{project_author}-{project_name}"

        # 根据项目名称创建新文件夹
        try:
            directory = os.path.join('algorithm', 'test_result', folder_name)

            os.makedirs(directory)
            file_path=os.path.join(directory,"log.txt")
            with open(file_path, "w") as file:
                file.write(f"Project Name: {project_name}\n")
                file.write(f"Project Author: {project_author}\n")
                file.write(f"Project Type: {project_type}\n")
                file.write(f"Project SingleDetermination: {project_SingleDetermination}\n")

            return JsonResponse({"status": "success", "message": "文件夹创建成功"})
        except FileExistsError:
            return JsonResponse({"status": "error", "message": "文件夹已存在"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"创建文件夹失败: {str(e)}"})
    else:
        return JsonResponse({"status": "error", "message": "无效的请求"})
    # if request.method == 'POST':
    #     data = json.loads(request.body)
    #     project_name = data.get('project_name')
    #     project_author = data.get('project_author')
    #
    #     # 根据项目名称和作者创建新文件夹，使用破折号作为分隔符
    #     folder_name = f"{project_author}-{project_name}"
    #     try:
    #         os.makedirs(folder_name)
    #         return JsonResponse({"status": "success", "message": "文件夹创建成功"})
    #     except FileExistsError:
    #         return JsonResponse({"status": "error", "message": "文件夹已存在"})
    #     except Exception as e:
    #         return JsonResponse({"status": "error", "message": f"创建文件夹失败: {str(e)}"})
    # else:
    #     return JsonResponse({"status": "error", "message": "无效的请求"})
