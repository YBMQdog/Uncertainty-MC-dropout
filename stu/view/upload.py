import os

from django.shortcuts import render, HttpResponse


# upload algorithm data into "/data"  file

def upload_list(request):
    if request.method == "GET":
        return render(request, 'upload_list.htmL')

    if request.method == "POST":

        type = request.POST.get('data type')

        if 'Train' in type:
            train_upload(request)

        elif 'Test' in type:
            test_upload(request)

        elif 'MC' in type:
            MC_upload(request)

    return HttpResponse("submit successfully...（￣︶￣）")


# for train data
def train_upload(request):
    files = request.FILES.getlist("avatar")
    print(files)

    for file in files:
        with open('%s' % os.path.join('data/train', file.name), 'wb') as f:
            for i in file.chunks():
                f.write(i)


# for test data
def test_upload(request):
    files = request.FILES.getlist("avatar")
    print(files)

    for file in files:
        with open('%s' % os.path.join('data/test', file.name), 'wb') as f:
            for i in file.chunks():
                f.write(i)


# for uncertainty measurement data
def MC_upload(request):
    files = request.FILES.getlist("avatar")
    print(files)

    for file in files:
        with open('%s' % os.path.join('data/test for mc', file.name), 'wb') as f:
            for i in file.chunks():
                f.write(i)
