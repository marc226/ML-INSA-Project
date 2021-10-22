import time

start_date = time.time()
print("Start time: " + str(time.strftime("%d.%m.%Y %H:%M:%S")))

import numpy as np
import cv2
import drawrecs
import nms
from pyramid import pyramid_sliding_window_detection
import load_data

#build neural network
net = load_data.net

end_date = time.time()
dauer = end_date - start_date
print("Network trained! Duration: " + str(int(dauer)) + "s")

def rec_faces(filepath, dest_path):
    #load image where faces should be detected
    print("load test image")
    image_for_tracking = filepath
    test_img = cv2.imread(image_for_tracking)
    gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY).astype(float)
    gray = gray/128.0 - 1.0

    #build bboxes
    print("building bboxes")
    bboxes2 = pyramid_sliding_window_detection(net,np.array(gray, dtype='float32'), 1.2, 36, 36, 5)

    #build frames using nms
    arr_boxes, keep = nms.nms_bboxes(bboxes2)
    print("nms sorted from " + str(len(arr_boxes)) + " to " + str(len(keep)))
    testrecs = []
    to_draw = []
    for to_keep in keep:
        to_draw += [arr_boxes[to_keep]]

    for scale in bboxes2:
        # Fürs Testen kann man bestimmte Rechteckgrößen bbevorzugen
        #i += 1
        #if (i<10): continue
        for element in scale[1]:
            #if len(element) == 4:
            toAdd = [element[0], element[1], element[2], element[3]]
            testrecs += [toAdd]

    #draw images
    print("Drawing image...")
    drawrecs.drawrec_mult(image_for_tracking, dest_path + "_before.jpg", testrecs)
    drawrecs.drawrec_mult(image_for_tracking, dest_path, to_draw)
    print("Image " + dest_path + " detected and drawn within " + str(int(time.time())) + "s. Exciting.")

#img_array: [[source,destination], [source,destination]]
def detect_multiple(img_array):
    i = 0
    for img in img_array:
        i += 1
        print("Processing image " + str(i) + " of " + str(len(img_array)))
        filepath = img + ".jpg"
        det_path = img + "_detected.jpg"
        rec_faces(filepath, det_path)

img_array = ["woman-ge619f8218_640","testbild2","testimg3","testimg","Testimg_gray", "Testimg_gray_lowcontrast", "WIN_20211021_12_46_40_Pro","WIN_20211021_12_46_51_Pro"]

detect_multiple(img_array)

print("Done! Duration of creating the net: " + str(int(end_date-start_date)) + "s")
duration_detection = time.time() - end_date
end_date = time.time()
dauer = end_date - start_date
print("Duration of detecting the images: " + str(int(duration_detection)) + "s")
print("Complete duration: " + str(int(dauer)) + "s")