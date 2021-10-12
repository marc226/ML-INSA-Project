import load_data
from pyramid import pyramid_sliding_window_detection
import numpy as np
import cv2
import load_data

net = load_data.net

test_img = cv2.imread("./testimg.jpg")
gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY).astype(float)
gray = gray/128.0 - 1.0

bboxes = pyramid_sliding_window_detection(net,np.array(gray, dtype='float32'), 1.2, 36, 36, 5)

print(bboxes)
