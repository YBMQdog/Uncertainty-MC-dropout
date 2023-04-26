import json
import os
import shutil

from PIL.Image import Image

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


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
