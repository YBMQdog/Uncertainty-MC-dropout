import base64
import io

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

    model = Net()
    model.to(device)
    model.load_state_dict(torch.load(model_file))
    model.train()
    dataset_dir = os.path.join(dataset_dir, 'Test_picture.jpg')

    result_list = nn.zeros(times)
    img = Image.open(dataset_dir)
    img_data = getdata.dataTransform(img).to(device)
    imgs_data = torch.unsqueeze(img_data, dim=0)

    result_file = 'algorithm/test_result'


    for a in range(times):
        out = model(imgs_data)
        out = F.softmax(out, dim=1)
        out = out.data.cpu().numpy()
        result_list[a] = out[0, 0]
        print(out)

        plt.figure()
        if out[0, 0] > out[0, 1]:
            plt.suptitle('cat:{:.1%},dog:{:.1%}'.format(out[0, 0], out[0, 1]))
        else:
            plt.suptitle('dog:{:.1%},cat:{:.1%}'.format(out[0, 1], out[0, 0]))

        plt.imshow(img)

        plt.savefig(os.path.join(result_file, "result{}.png".format(a)))

        plt.clf()
        plt.close()

    return result_list


def draw_result(list, mean, var, length, data_dir):
    # Print messages


    # Round variance and mean
    var = round(var, 5)
    mean = round(mean, 3)

    # Set width of bars in bar chart
    width = 0.5

    # Initialize x and y lists for bar chart
    x_list = nn.zeros(length)
    y_list = list

    # Set font for plot
    plt.rcParams["font.sans-serif"] = ['SimHei']
    plt.rcParams["axes.unicode_minus"] = False

    # Create x values for bar chart
    for i in range(length):
        x_list[i] = i + 1

    # Plot bar chart
    plt.bar(i + 1, list[i], width, label=('prediction' + str(i + 1)))

    # Plot horizontal line at mean value
    plt.axhline(mean)

    # Set labels and title for plot
    plt.xlabel("times")
    plt.title("variance is " + str(var))

    # Set y limits for plot
    plt.ylim(0, 1)

    # Set y label for plot
    plt.ylabel("probability")

    # Create path to save plot
    data_dir = os.path.join(data_dir, 'detail')

    # Print path to save plot


    # Save plot to file
    plt.savefig(os.path.join(data_dir, f"variance for times{length}"))

    # Clear plot
    plt.clf()


# 计算方差
def calculation(list, T, data_dir):
    # Print messages
    print('this is calculation part')


    # Initialize mean, variance and length
    mean = 0.00
    var = 0.00
    length = 0;

    # Calculate the sum of the first T elements
    for i in range(T):
        mean = list[i] + mean
        length = length + 1

    # Calculate the mean
    mean = mean / T
    print("the average value is "+str(mean))

    # Calculate the variance
    for a in range(T):
        var = (list[a] - mean) ** 2 + var
    var = var / T

    # Call the draw_result function to draw the result
    draw_result(list, mean, var, length, data_dir)

    # Print the result
    print('the times is ' + str(T) + 'the variance is' + "%.6f" % var)

    # Return the mean and variance
    return mean, var


def main(directory, number):
    path_data = os.path.join(directory, 'detail')
    dataset_dir = directory

    model_file = os.path.join('algorithm\model', 'model.pth')


    clean(path_data)

    x_list = nn.zeros(1000)
    y_list = nn.zeros(1000)

    times = int(number)

    for i in (n + 1 for n in range(times)):
        print("this is  cycle" + str(i))
        result = test(i, dataset_dir, model_file)
        print(result)
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
    plt.savefig(os.path.join(directory, "uncertainty_chart"))
    # 创建一个BytesIO对象
    buf = io.BytesIO()

    # 将图像保存到BytesIO对象中
    plt.savefig(buf, format='png')

    # 关闭图像
    plt.close()

    # 将BytesIO对象的内容转换为Base64字符串
    image_str = base64.b64encode(buf.getvalue()).decode('utf-8')

    # 返回Base64编码的图像字符串
    return image_str


if __name__ == '__main__':
    main()
