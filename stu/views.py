import json
import os
import shutil


from PIL.Image import Image
from algorithm.Uncertainty_test import main
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from myproject import settings


def create_users(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        project_name = data.get('project_name')
        project_author = data.get('project_author')
        project_type = data.get(' project_type')
        project_SingleDetermination = data.get('Project_SingleDetermination')
        folder_name = f"{project_author}-{project_name}"

        # 根据项目名称创建新文件夹
        try:
            directory = os.path.join('algorithm', 'test_result', folder_name)

            os.makedirs(directory)
            file_path = os.path.join(directory, "log.txt")
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


def delete_users(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        project_name = data.get('project_name')
        project_author = data.get('project_author')

        # 拼接项目名称和作者的文件夹名称
        folder_name = f"{project_author}-{project_name}"
        directory = os.path.join('algorithm', 'test_result', folder_name)

        try:
            # 删除文件夹
            shutil.rmtree(directory)
            return JsonResponse({"status": "success", "message": "文件夹删除成功"})
        except FileNotFoundError:
            return JsonResponse({"status": "error", "message": "文件夹不存在"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"删除文件夹失败: {str(e)}"})
    else:
        return JsonResponse({"status": "error", "message": "无效的请求"})



def handle_uploaded_file(f,directory):

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file.endswith('.jpg'):
            os.remove(file_path)

        # 保存新上传的文件
        with open(os.path.join(directory, 'Test_picture.jpg'), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':

        project_name = request.POST.get('project_name')
        project_author = request.POST.get('project_author')

        folder_name = f"{project_author}-{project_name}"
        directory = os.path.join('algorithm', 'test_result', folder_name)
        handle_uploaded_file(request.FILES['avatar'], directory)

        return HttpResponse('Upload successful!')
    return render(request, 'upload.html')

def Uncertainty_run(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        project_name = data.get('project_name')
        project_author = data.get('project_author')

        Test_number = data.get('TestParameters')

        folder_name = f"{project_author}-{project_name}"
        directory = os.path.join('algorithm', 'test_result', folder_name)

        detail_directory = os.path.join(directory, 'detail')
        os.makedirs(detail_directory, exist_ok=True)
        main(directory,Test_number)
        response_data = {'status': 'success', 'message': '项目已运行'}
        return JsonResponse(response_data)
    return render(request, 'run.html')