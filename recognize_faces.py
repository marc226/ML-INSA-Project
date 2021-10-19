import numpy as np
import cv2
import drawrecs
import nms
#from pyramid import pyramid_sliding_window_detection
#import load_data

#net = load_data.net

#bboxes2 = pyramid_sliding_window_detection(net,np.array(gray, dtype='float32'), 1.2, 36, 36, 5)


print("load test image")

test_img = cv2.imread("./testimg.jpg")
gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY).astype(float)
gray = gray/128.0 - 1.0

print("building bboxes")

import bboxes
bboxes2 = bboxes.bboxes1


#Zum Testen kann bboxes als txt file gespeichert werden, um von da weiter zu arbeiten, ohne das Netzwerk immer neu aufbauen zu müssen
with open('bboxes.txt', 'a') as writeTo:
    writeTo.write(str(bboxes2))
print("bboxed built!")

arr_boxes, keep = nms.nms_bboxes(bboxes2)

testrecs = []

for scale in bboxes2:
    # Fürs Testen kann man bestimmte Rechteckgrößen bbevorzugen
    #i += 1
    #if (i<10): continue
    for element in scale[1]:
        #if len(element) == 4:
        toAdd = [element[0], element[1], element[2]-element[0], element[3]-element[1]]
        testrecs += [toAdd]


to_draw = []
for to_keep in keep:
    to_draw += [arr_boxes[to_keep]]


drawrecs.drawrec_mult("testimg.jpg", "testout.jpg", to_draw)
drawrecs.drawrec_mult("testimg.jpg", "testout_mit_allen.jpg", testrecs)

print("Image drawn. Exiting.")