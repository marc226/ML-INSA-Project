import numpy as np
import torch
import torchvision
import torch.optim as optim
import torch.nn as nn
from net import Net
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from torch.utils.data.sampler import SubsetRandomSampler


def test_after_epoch(index):
    correct = 0
    total = 0
    with torch.no_grad():
        for dataTest in test_loader:
            imagesTest, labelsTest = dataTest
            outputsTest = net(imagesTest)
            _, predicted = torch.max(outputsTest.data, 1)
            total += labelsTest.size(0)
            correct += (predicted == labelsTest).sum().item()
    print("Testing")
    overfit_index.append(index)
    overfit_array.append(100 * correct / total)
    print('Accuracy of the network on the test images: %d %%' % (
            100 * correct / total))

train_dir = './03medium'
test_dir = './test_images'

transform = transforms.Compose(
    [transforms.Grayscale(),
     transforms.ToTensor(),
     transforms.Normalize(mean=(0,),std=(1,))])

train_data = torchvision.datasets.ImageFolder(train_dir, transform=transform)
test_data = torchvision.datasets.ImageFolder(test_dir, transform=transform)

valid_size = 0.2
batch_size = 32

num_train = len(train_data)
indices_train = list(range(num_train))
np.random.shuffle(indices_train)
split_tv = int(np.floor(valid_size * num_train))
train_new_idx, valid_idx = indices_train[split_tv:],indices_train[:split_tv]

train_sampler = SubsetRandomSampler(train_new_idx)
valid_sampler = SubsetRandomSampler(valid_idx)

train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, sampler=train_sampler)
valid_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, sampler=valid_sampler)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=True)

classes = ('noface','face')
net = Net()

# for epoch in range(1, n_epochs+1):
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
""", weight_decay=0.0001"""

#Visual variables
loss_array = []
loss_indicator = []
step = 0
epoch_array = []
epoch_indicator = []
epoch_index = 1
epoch_indicator.append(0)
epoch_array.append(1)
overfit_index = []
overfit_array = []
epoch_count = 0

for epoch in range(16):  # loop over the dataset multiple times
    print("epoch: " + str(epoch))
    running_loss = 0.0
    varEnum = enumerate(train_loader)
    if epoch > 0:
        test_after_epoch(epoch)
    for i, data in enumerate(train_loader):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 200 == 199:    # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 200))
            step += 200
            loss_array.append(running_loss/200)
            loss_indicator.append(step)
            running_loss = 0.0
    epoch_indicator.append(step)
    epoch_array.append(epoch_index)
    epoch_index += 1


print('Finished Training')
# for data, target in train_loader:

"""
test_loss = 0.0
count = 0
for i, data in enumerate(test_loader):
    inputs, labels = data
    outputs = net(inputs)
    loss = criterion(outputs, labels)
    count = i
    test_loss = loss.item
avg_loss = test_loss / count
"""

with open('overfitting_data.txt', 'a') as writeTo:
    writeTo.write("\n\n")
    writeTo.write(str(overfit_index))
    writeTo.write("\n")
    writeTo.write((str(overfit_array)))

fig, loss_plot = plt.subplots()
loss_plot.plot( loss_indicator,loss_array, color ="red", label = "Loss function")
loss_plot.set_xlabel("Batches processed")
loss_plot.set_ylabel("Average loss function")

epoch_plot = loss_plot.twinx()
epoch_plot.step( epoch_indicator, epoch_array, color = "gray", label = "Epoch")
epoch_plot.set_ylabel("Epoch #")
plt.legend()
plt.show()
fig.savefig('Loss function_epoch plot.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')

fig2 = plt.figure(2)
plt.title("Overfitting curve")
plt.plot(overfit_index, overfit_array)
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.show()
# save the plot as a file



