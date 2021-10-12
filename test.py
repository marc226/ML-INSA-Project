import torch
import load_data

correct = 0
trainedNet = load_data.net
total = 0
with torch.no_grad():
    for data in load_data.test_loader:
        images, labels = data
        outputs = trainedNet(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print('Accuracy of the network on the 10000 test images: %d %%' % (
    100 * correct / total))

