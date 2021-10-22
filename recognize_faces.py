import time

start_date = time.time()
print("Start time: " + str(time.strftime("%d.%m.%Y %H:%M:%S")))

print("Info: Sometimes you have to restart the program, if in the second epoch the loss is still exactly 0.693")

import numpy as np
import cv2
import drawrecs
import nms
from pyramid import pyramid_sliding_window_detection
import build_and_train_net

#build neural network
net = build_and_train_net.net

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

img_array = ["images_for_detection/woman-ge619f8218_640","images_for_detection/testbild2","images_for_detection/testimg3",
"images_for_detection/testimg","images_for_detection/Testimg_gray",
 "images_for_detection/WIN_20211021_12_46_40_Pro","images_for_detection/WIN_20211021_12_46_51_Pro"]

detect_multiple(img_array)

print("Done! Duration of creating the net: " + str(int(end_date-start_date)) + "s")
duration_detection = time.time() - end_date
end_date = time.time()
dauer = end_date - start_date
print("Duration of detecting the images: " + str(int(duration_detection)) + "s")
print("Complete duration: " + str(int(dauer)) + "s")