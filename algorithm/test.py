from network import Net
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
from PIL import Image
import random
import os
import getdata

dataset_dir = './data/test/'
model_file = './model/model.pth'
N = 10

device = torch.device("cuda:0" if (torch.cuda.is_available()) else "cpu")


def test():

    model = Net()
    model.to(device)
    model.load_state_dict(torch.load(model_file))
    model.eval()
    files = random.sample(os.listdir(dataset_dir), N)
    imgs = []
    imgs_data = []
    for file in files:
        img = Image.open(dataset_dir + file)
        img_data = getdata.dataTransform(img).to(device)
        imgs.append(img)
        imgs_data.append(img_data)
    imgs_data = torch.stack(imgs_data)
    out = model(imgs_data)
    out = F.softmax(out, dim=1)
    out = out.data.cpu().numpy()
    def del_file(path_data):
        for i in os.listdir(path_data):
            file_data = path_data + "\\" + i
            if os.path.isfile(file_data) == True:
                os.remove(file_data)
            else:
                del_file(file_data)

    path_data = r"./test_result"
    del_file(path_data)
    for idx in range(N):
        plt.figure()
        if out[idx, 0] > out[idx, 1]:
            plt.suptitle('cat:{:.1%},dog:{:.1%}'.format(out[idx, 0], out[idx, 1]))
        else:
            plt.suptitle('dog:{:.1%},cat:{:.1%}'.format(out[idx, 1], out[idx, 0]))
        plt.imshow(imgs[idx])
        plt.savefig("./test_result/result{}.png".format(idx))


if __name__ == '__main__':
    test()


