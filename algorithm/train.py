from torch.utils.data import DataLoader as DataLoader
from getdata import DogsVSCatsDataset as DVCD
from network import Net
import torch
from torch.autograd import Variable

dataset_dir = './data/'  # data
model_cp = './model/'  # model storage
workers = 10
batch_size = 16
lr = 0.0001  # learning rate
nepoch = 1

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")


def train():
    datafile = DVCD('train', dataset_dir)
    dataloader = DataLoader(datafile, batch_size=batch_size, shuffle=True, num_workers=workers,
                            drop_last=True)

    print('Dataset loaded! length of train set is {0}'.format(len(datafile)))
    model = Net()
    model = model.to(device)
    model.train()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = torch.nn.CrossEntropyLoss()

    cnt = 0
    for epoch in range(nepoch):

        for img, label in dataloader:
            img, label = Variable(img).to(device), Variable(label).to(
                device)
            out = model(img)
            loss = criterion(out,
                             label.squeeze())
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            cnt += 1
            print('Epoch:{0},Frame:{1}, train_loss {2}'.format(epoch, cnt * batch_size,
                                                               loss / batch_size))

    torch.save(model.state_dict(), '{0}/model.pth'.format(model_cp))


if __name__ == '__main__':
    train()
