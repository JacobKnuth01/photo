import cv2
import PIL.Image
import numpy as np
import random
import math

def BlankColor(rgb, r=250, c=250):
    #Returns a r X c array of the rgb color
    pic = []
    for _ in range(r):
        l = []
        for _ in range(c):
            l.append(rgb)
        pic.append(l)
    pic = np.array(pic)
    pic = pic.astype(np.uint8)
    return pic

def copy(pic):
    # copys a picture array
    pic = pic.astype(np.uint8)
    new = []
    r = len(pic)
    c = len(pic[0])
    for rows in range(r):
        l = []
        for col in range(c):
            l.append(pic[rows][col])
        new.append(l)
    new = np.array(new)
    new = new.astype(np.uint8)
    return new

def swap(backround, top, color, tolerance, percents=False):
    # if backround pixle == color then replace that pixle with top image
    r = 0
    c = 0
    pic = copy(backround)

    while r < len(pic):
        while c < len(pic[r]):

            try:
                bcolor = backround[r][c]
                topColor = top[r][c]
                replace = True


                for i in range(3):
                    if tolerance == 0:
                        if bcolor[i] != color[i]:
                            replace = False
                    else:
                        ran = range(color[i] - tolerance, color[i] + tolerance)
                        if bcolor[i] not in ran:
                            replace = False


                if replace:
                    pic[r][c] = topColor


            except IndexError:
                pass

            c = c +1
        c = 0
        if percents:
            print(f"{r/len(pic)*100:.2f}%")
        r = r +1
    return pic
def gen3D(r, c):
    # creates a random pic of r X c
    threeD = []

    for rows in range(r):
        l = []
        for col in range(c):
            n1 = random.randint(0, 255)
            n2 = random.randint(0, 255)
            n3 = random.randint(0,255)
            l.append([n1,n2,n3])
        threeD.append(l)
    threeD = np.array(threeD)
    threeD = threeD.astype(np.uint8)
    return threeD


def circle(spot, screen, radius, color = [255,0,0]):
    c = 0
    r = 0
    pic = copy(screen)
    while r < len(pic):
        while c < len(pic[r]):
            if math.sqrt((c-spot[0])**2 + (r-spot[1])**2) <= radius:
                try:

                    pic[r][c] = color
                except IndexError:

                    pass
            c = c +1
        c = 0
        r = r +1
    return pic
def allColorDisplay():
    master = []
    for i in range(256):
        for w in range(256):
            for z in range(256):


                array = BlankColor([i,w,z ], r =1, c=1)
                master.append(array)
    final = np.concatenate(master)



    return final


if __name__ == "__main__":
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    path = r"C:\Users\knuth\Pictures\big-blue-sky-deep-blue-ocean-013.jpg"
    i = PIL.Image.open(path)
    i = np.array(i)
    while True:
        good, frame = camera.read()
        frame = swap(frame,i,[0,0,0], 10, percents=True)
        cv2.imshow("screen",frame)
        cv2.waitKey(1)