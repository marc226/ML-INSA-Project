from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#Takes an address of an image, a destination address, and a list of rectangles
#List of rectangles as follows: [[x,y,width,height],...]
#Plots the rectangles into the images and saves it
def drawrec_mult(image_src, image_dest, rect_list):
    source_img = Image.open(image_src).convert("RGB")
    draw = ImageDraw.Draw(source_img)
    for rect in rect_list:
        x = rect[0]
        y = rect[1]
        size_x = rect[2]
        size_y = rect[3]
        draw.rectangle(((x, y), (x+size_x, y+size_y)), outline = "red")
    out_file = "output_test.jpeg"
    source_img.save(out_file, "JPEG")

#Takes an address of an image, a destination address, and a list of rectangles
#List of rectangles as follows: [[x,y,width,height,linewidth],...]
#Plots the rectangles into the images and saves it
def drawrec_mult_lw(image_src, image_dest, rect_list):
    image_array = mpimg.imread(image_src)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for rect in rect_list:
        x = rect[0]
        y = rect[1]
        size_x = rect[2]
        size_y = rect[3]
        width = rect[4]
        rect = plt.Rectangle((x, y), size_x, size_y, fill=False, edgecolor = 'red',linewidth=width)
        ax.add_patch(rect)
        plt.imshow(image_array)
    fig.savefig(image_dest)

#Takes an address of an image, a destination address, and proportions of a rectangle
#Plots the rectangles into the images and saves it
def drawrec(image_src, x, y, size_x, size_y):

    source_img = Image.open(image_src).convert("RGB")
    draw = ImageDraw.Draw(source_img)
    draw.rectangle(((x, y), (x+size_x, y+size_y)), outline = "red")
    out_file = "output_test.jpeg"
    source_img.save(out_file, "JPEG")

#Takes an address of an image, a destination address, and proportions of a rectangle plus a linewidth
#Plots the rectangles into the images and saves it
def drawrec_lw(image_src, image_dest, x, y, size_x, size_y, linewidth):
    image_array = mpimg.imread(image_src)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    rect = plt.Rectangle((x, y), size_x, size_y, fill=False, edgecolor = 'red',linewidth=linewidth)
    ax.add_patch(rect)
    plt.imshow(image_array) # Bildarray
    #plt.show()
    fig.savefig(image_dest)

#Example (Bild1.png is some image in folder):
entry1 = [1,1,100,100,3]
entry2 = [200,200,20,40,2]
list_rec = [entry1,entry2]
drawrec_mult_lw("Bild1.png", "output_test.jpeg", list_rec)
#drawrec("Bild1.png", 200, 300, 100, 100)