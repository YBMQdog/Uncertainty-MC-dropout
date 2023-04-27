from PIL.Image import Image
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from stu import models


# Create your views here.

def index(request):
    return HttpResponse('hello world!')


def test(request):
    return HttpResponse('good evening!')


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