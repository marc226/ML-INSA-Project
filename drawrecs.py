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
        draw.rectangle(((x, y), (size_x, size_y)), outline = "red")
    source_img.save(image_dest, "JPEG")

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