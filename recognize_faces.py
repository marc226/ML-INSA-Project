import numpy as np
import cv2
import drawrecs
from pyramid import pyramid_sliding_window_detection
import load_data

net = load_data.net

print("load test image")

test_img = cv2.imread("./testimg.jpg")
gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY).astype(float)
gray = gray/128.0 - 1.0

print("building bboxes")

bboxes = pyramid_sliding_window_detection(net,np.array(gray, dtype='float32'), 1.2, 36, 36, 5)

#Zum Testen kann bboxes als txt file gespeichert werden, um von da weiter zu arbeiten, ohne das Netzwerk immer neu aufbauen zu müssen
#with open('bboxes.txt', 'a') as writeTo:
#    writeTo.write(str(bboxes))
print("bboxed built!")

#i = 0
rectangles = []
for scale in bboxes:
    # Fürs Testen kann man bestimmte Rechteckgrößen bbevorzugen
    #i += 1
    #if (i<10): continue
    for element in scale[1]:
        if len(element) == 4:
            toAdd = [element[0], element[1], element[2]-element[0], element[3]-element[1]]
            rectangles += [toAdd]

#print(rectangles)

drawrecs.drawrec_mult("testimg.jpg", "testout.jpg", rectangles)

print("Image drawn. Exiting.")