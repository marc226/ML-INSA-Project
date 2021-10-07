import os
from shutil import copyfile
import time

from random import sample

def choice(desired):
    files = os.listdir('./train_images_test/1/')
    i = 0
    for file in sample(files,desired):
        #os.remove('/train_images_test/1/'+ file)
        newpath = "ausgewaehlt"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        copyfile('./train_images/1/' + file, './ausgewaehlt/' + file)
        if(i%10000 == 0):
            print(i)
        i += 1
    print("done choosing")

def duplicate(desired):
    aktuell = 0
    files = os.listdir('./train_images_test/0/')
    i = aktuell
    loop = 0
    newpath = "duplicated"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    while (aktuell < desired):
        if((desired - aktuell) < aktuell): to_dup = desired - aktuell
        else: to_dup = 26950
        print("to_dup: " + str(to_dup))
        for file in sample(files, to_dup):
            copyfile('./train_images_test/0/' + file, './duplicated/' + str(loop) + file)
            i += 1
            if(i%10000 == 0): print("duplicated: " + str(i))
        aktuell += to_dup
        loop += 1

def auswahl():
    newpath = "01small"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = "01small/0"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = "01small/1"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    #0_nofaces
    files = os.listdir('./train_images_test/0/')
    print("Copying no faces...")
    for file in files:
        copyfile('./train_images_test/0/' + file, './01small/0/' + file)
    print("Copying done!")

    #1_faces
    files = os.listdir('./train_images_test/1/')
    choice(26950)
    to_move = os.listdir('./ausgewaehlt/')
    print('copying files to destination')
    i = 0
    for file in to_move:
        copyfile('./ausgewaehlt/' + file, './01small/1/' + file)
        os.remove('./ausgewaehlt/' + file)
        i += 1
        if(i%10000 == 0): print("copied: " + str(i))


def hochrechnen():
    print("Hochrechnen....")
    newpath = "02big"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = "02big/0"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = "02big/1"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    #0nofaces
    print("duplicating nofaces")
    duplicate(64770)
    to_move = os.listdir('./duplicated/')
    print("Copying files")
    for file in to_move:
        copyfile('./duplicated/' + file, './02big/0/' + file)
        os.remove("./duplicated/" + file)
    
    #1faces
    print("choosing faces")
    files = os.listdir('./train_images_test/1/')
    print("Copying faces...")
    i = 0
    for file in files:
        copyfile('./train_images_test/1/' + file, './02big/1/' + file)
        i += 1
        if(i%10000 == 0): print("copied: " + str(i))
    print("Copying done!")


def mitteln():
    print("Mitteln")
    newpath = "03medium"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = "03medium/0"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = "03medium/1"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    #0nofaces
    print("duplicating nofaces")
    duplicate(45860)
    to_move = os.listdir('./duplicated/')
    i = 0
    for file in to_move:
        copyfile('./duplicated/' + file, './03medium/0/' + file)
        os.remove('./duplicated/' + file)
        i += 1
        if(i%10000 == 0): print("copied: " + str(i))
    
    #1faces
    print("choosing faces")
    choice(45860)
    to_move = os.listdir('./ausgewaehlt/')
    i = 0
    print("start copying")
    for file in to_move:
        copyfile('./ausgewaehlt/' + file, './03medium/1/' + file)
        os.remove('./ausgewaehlt/' + file)
        i += 1
        if(i%10000 == 0): print("copied: " + str(i))


start_date = time.time()
print("Start time: " + str(time.strftime("%d.%m.%Y %H:%M:%S")))

auswahl()
hochrechnen()
mitteln()

newpath = "ausgewaehlt"
if os.path.exists(newpath):
    os.remove(newpath)
newpath = "duplicated"
if os.path.exists(newpath):
    os.remove(newpath)

end_date = time.time()
dauer = end_date - start_date
print("Fertig! Gesamte Dauer: " + str(dauer))