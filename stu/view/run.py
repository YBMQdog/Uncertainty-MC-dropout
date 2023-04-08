from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def run(request):
    if request.method == "GET":
       messages.success(request, "running!")
    return render(request,'run_result.html')

