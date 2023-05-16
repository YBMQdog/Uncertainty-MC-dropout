from network import Net
from network import Net
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
from PIL import Image
import random
import os
import getdata
model_file = './model/model.pth'
device = torch.device("cuda:0" if (torch.cuda.is_available()) else "cpu")

def model_info():
    model = Net()
    model.to(device)
    model.load_state_dict(torch.load(model_file))

    print("Model's state_dict:")
    for param_tensor in model.state_dict():
      print(param_tensor, "\t", model.state_dict()[param_tensor].size())


if __name__ == '__main__':
    model_info()