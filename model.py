import torch.nn as nn
import torch

# Modified from Tutorial 3a and lecture notes
class CNNalex(nn.Module):
    def __init__(self):
        super(CNNalex, self).__init__()
        # nn.Conv2d(256,300,5,2)
        self.conv1 = nn.Conv2d(256,300,3, padding = 2) # Modified to 3, in_channels, out_chanels, kernel_size
        self.bn1 = nn.BatchNorm2d(300)
        self.conv2 = nn.Conv2d(300,350,3)
        self.bn2 = nn.BatchNorm2d(350)

        self.pool = nn.MaxPool2d(2, 2) #kernel_size, stride 
        self.fc1 = nn.Linear(350*2*2, 32) # Modified first parameter
        self.fc2 = nn.Linear(32, 7)

    def forward(self, x):
        x = self.pool(self.relu(self.bn1(self.conv1(x))))#4
        x = self.relu(self.bn2(self.conv2(x)))#2
        x = x.view(-1, 350*2*2) # Modified size
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x


if __name__ == '__main__':
    bn_model = CNNalex()
    x = torch.randn(1,1,48,48)
    print('Shape of output = ',bn_model(x).shape)
    print('No of Parameters of the BatchNorm-CNN Model =',bn_model.count_parameters())