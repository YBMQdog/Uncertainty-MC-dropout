from network import Net
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
from PIL import Image
import random
import os
import getdata
import numpy as nn

dataset_dir = './data/test for MC/'
model_file = './model/model.pth'
figure_save_path ='./test_result'
path_data = r"./test_result"
N = 1

device = torch.device("cuda:0" if (torch.cuda.is_available()) else "cpu")
def clean():
    for i in os.listdir(path_data):
            file_data = path_data + "\\" + i
            if os.path.isfile(file_data) == True:
                os.remove(file_data)
            else:
                clean()




def test(times):
    model = Net()
    model.to(device)
    model.load_state_dict(torch.load(model_file))
    model.eval()
    files = random.sample(os.listdir(dataset_dir), N)
    imgs = []
    imgs_data = []
    result_list = nn.zeros(200)
    for file in files:
        img = Image.open(dataset_dir + file)
        img_data = getdata.dataTransform(img).to(device)
        imgs.append(img)
        imgs_data.append(img_data)
    imgs_data = torch.stack(imgs_data)


    for a in range(times):
        out = model(imgs_data)
        out = F.softmax(out, dim=1)
        out = out.data.cpu().numpy()
        result_list[a] = out[0, 0]


    return result_list

def draw_result(list,mean,var,length):
    var=round(var,5)
    mean=round(mean,3)
    width=0.5
    x_list=nn.zeros(length)
    y_list=list
    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False
    for i in range(length):
        x_list[i]=i+1

        plt.bar(i+1,list[i],width,label=('prediction'+str(i+1)))


    for a, b, c in zip(x_list, y_list, range(len(x_list))):
        plt.text(a, b + 0.01, "%.2f" % y_list[c], ha='center', fontsize=15)

    plt.axhline(mean)
    plt.xlabel("times")
    plt.title("variance is "+str(var))
    plt.ylim(0,1)
    plt.ylabel("probability")

    plt.savefig("./test_result/variance for times{}".format(length))
    plt.show()




def calculation(list,T):
    mean=0.00
    var=0.00
    length=0;

    for i in range(T):

        mean=list[i]+mean
        length=length+1



    mean=mean/T
    for a in range(T):
        var=(list[a]-mean)**2+var


    var=var/T
    draw_result(list,mean,var,length)
    print('the times is '+str(T)+'the variance is'+"%.6f"%var)
    return mean,var


if __name__ == '__main__':
    clean()
    plt.clf()

    x_list = nn.zeros(1000)
    y_list = nn.zeros(1000)
    times=input("how many times you want to test?")
    times=int(times)
    for i in (n + 1 for n in range(times)):
        print(i)
        result = test(i)
        var = calculation(result, i)

        x_list[i] = i
        y_list[i] = var[1]

    plt.plot(y_list)

    plt.xlim(0, times)
    plt.ylim(0, 0.01)
    plt.xlabel('times')
    plt.ylabel('variance')
    plt.title('Uncertainty')
    plt.grid(True)
    plt.show()





