from .network import Net
import torch
import torch.nn.functional as F
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
import random
import os
from . import getdata

import numpy as nn

path_data = r"./test_result"
N = 1

device = torch.device("cuda:0" if (torch.cuda.is_available()) else "cpu")


def clean(path):
    for i in os.listdir(path):
        file_data = path + "\\" + i
        if os.path.isfile(file_data) == True:
            os.remove(file_data)
        else:
            clean()


def test(times, dataset_dir, model_file):
    # print('zhe shi test ')
    # print(times)
    # print(dataset_dir)
    # print(model_file)
    model = Net()
    model.to(device)
    model.load_state_dict(torch.load(model_file))
    model.eval()
    dataset_dir = os.path.join(dataset_dir, 'Test_picture.jpg')
    # print(dataset_dir)

    result_list = nn.zeros(200)
    img = Image.open(dataset_dir)
    img_data = getdata.dataTransform(img).to(device)
    imgs_data = torch.unsqueeze(img_data, dim=0)

    for a in range(times):
        out = model(imgs_data)
        out = F.softmax(out, dim=1)
        out = out.data.cpu().numpy()
        result_list[a] = out[0, 0]

    return result_list


def draw_result(list, mean, var, length, data_dir):
    print('this is draw_result')
    print(data_dir)
    var = round(var, 5)
    mean = round(mean, 3)
    width = 0.5
    x_list = nn.zeros(length)
    y_list = list
    plt.rcParams["font.sans-serif"] = ['SimHei']
    plt.rcParams["axes.unicode_minus"] = False
    for i in range(length):
        x_list[i] = i + 1

        plt.bar(i + 1, list[i], width, label=('prediction' + str(i + 1)))

    # for a, b, c in zip(x_list, y_list, range(len(x_list))):
    #     plt.text(a, b + 0.01, "%.2f" % y_list[c], ha='center', fontsize=15)

    plt.axhline(mean)
    plt.xlabel("times")
    plt.title("variance is " + str(var))
    plt.ylim(0, 1)
    plt.ylabel("probability")

    data_dir = os.path.join(data_dir, 'detail')
    print(data_dir)
    plt.savefig(os.path.join(data_dir, f"variance for times{length}"))
    plt.clf()



def calculation(list, T, data_dir):
    print('this is calculation')
    print(data_dir)
    mean = 0.00
    var = 0.00
    length = 0;

    for i in range(T):
        mean = list[i] + mean
        length = length + 1

    mean = mean / T
    for a in range(T):
        var = (list[a] - mean) ** 2 + var

    var = var / T
    draw_result(list, mean, var, length, data_dir)
    print('the times is ' + str(T) + 'the variance is' + "%.6f" % var)
    return mean, var


def main(directory, number):
    path_data = os.path.join(directory, 'detail')
    dataset_dir = directory

    model_file = os.path.join('algorithm\model', 'model.pth')
    print(path_data)
    print(model_file)

    clean(path_data)


    x_list = nn.zeros(1000)
    y_list = nn.zeros(1000)
    print(number)

    times = int(number)

    for i in (n + 1 for n in range(times)):
        result = test(i, dataset_dir, model_file)
        var = calculation(result, i, dataset_dir)

        x_list[i] = i
        y_list[i] = var[1]

    plt.plot(y_list)

    plt.xlim(0, times)
    plt.ylim(0, 0.01)
    plt.xlabel('times')
    plt.ylabel('variance')
    plt.title('Uncertainty')
    plt.grid(True)
    plt.savefig(os.path.join(directory, "uncertainty chart"))


if __name__ == '__main__':
    main()
