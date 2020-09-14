import cv2
from pytesseract import pytesseract #Tessaract for ocr
from PIL import Image #PythonImage Library
import numpy as np #numerical python file
import os #Operating System 
from Barcode import Barcode_Scanner #Barcpde scanner is for barcodes

# Files Reader 
def filesaver(filname, text):
    f = open(filname, "w+")
    for i in range(len(text)):
        f.write(f"{text[i]}")
    f.close()

# gray scale
def gray(img):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("img_gray.png",img)
    return img


# blur
def blur(img) :
    img_blur = cv2.GaussianBlur(img,(5,5),0)
    cv2.imwrite("img_blur.png",img)    
    return img_blur


# threshold
def threshold(dir_, file_, total):
    print(total, dir_, file_)
    #pixels with value below 100 are turned black (0) and those with higher value are turned white (255)
    for i in range(len(file_)):
        print(i)
        print(file_[i])
        img = cv2.imread(os.path.join(dir_, file_[i]), 0)
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]    
        gray = cv2.bitwise_not(img)
        kernel = np.ones((2, 1), np.uint8)
        img = cv2.erode(gray, kernel, iterations=1)
        img = cv2.dilate(img, kernel, iterations=1)
        #print(os.path.exists(os.path.join(dir_+f"/{file_}"+"thres", file_)), os.path.join(dir_+f"/{file_}"+"thres", file_))
        if os.path.exists(os.path.join(dir_+"/", file_[i]+"thres")):
            pass
        else:
            path = os.path.join(dir_+"/", file_[i]+"thres")
            os.mkdir(path)
            cv2.imwrite(path+f"/{file_[i]}+thres.png", img)
            out_below = pytesseract.image_to_string(img)
            print("out_below",  out_below)
            filesaver(path+f"/{file_[i]}+thres.txt", out_below)
            print(path)
            cropimage, textfile = Barcode_Scanner(path_to_image=os.path.join(dir_, file_[i]))
            cv2.imwrite(path+f"/{file_[i]}+cropimg.png", cropimage)
            filesaver(path+f"/{file_[i]}+decode.txt", textfile)


def collectimages():
    dirname_li = []
    filenames_li = []
    total_path = []
    for dirname, _, filenames in os.walk(os.getcwd()+'/package_images'):
        for filename in filenames:
            if os.path.join(dirname, filename).endswith('.jpeg') or os.path.join(dirname, filename).endswith('.jpg'):
                dirname_li.append(dirname)
                filenames_li.append(filenames)
                total_path.append(os.path.join(dirname, filename))
            else:
                pass
    
    return dirname_li, filenames_li, total_path


if __name__ == "__main__":
    dir_, file_, total = collectimages()
    for i in range(len(dir_)):
        threshold(dir_[i], file_[i], total[i])