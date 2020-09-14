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
def threshold(dir_, file_):
    print(dir_, file_)
    #pixels with value below 100 are turned black (0) and those with higher value are turned white (255)
    for i in range(len(file_)):
        
        img = cv2.imread(os.path.join(dir_, file_[i]), 0)
        print(os.path.join(dir_, file_[i]))
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.threshold(img, 0, 255, cv2.THRESH_TOZERO | cv2.THRESH_TOZERO)[1]    
        gray = cv2.bitwise_not(img)
        kernel = np.ones((2, 1), np.uint8)
        img = cv2.erode(gray, kernel, iterations=2)
        img = cv2.dilate(img, kernel, iterations=2)
        #print(gray)
        #print(len([i for i in (os.listdir(os.path.join(dir_+"/", file_[i]+"thres"))) ]))
        print(dir_+f"/{file_[i]}"+"thres")
        if os.path.exists(os.path.join(dir_+"/", file_[i]+"thres")):

            path = os.path.join(dir_+"/", file_[i]+"thres")
            cv2.imwrite(path+f"/{file_[i]}+thres.png", img)
            out_below = pytesseract.image_to_string(img)
            #print("out_below",  out_below)
            filesaver(path+f"/{file_[i]}+thres.txt", out_below)
            #print(path)
            cropimage, textfile = Barcode_Scanner(path_to_image=os.path.join(dir_, file_[i]))
            cv2.imwrite(path+f"/{file_[i]}+cropimg.png", cropimage)
            filesaver(path+f"/{file_[i]}+decode.txt", textfile)

        else:
            path = os.path.join(dir_+"/", file_[i]+"thres")
            os.mkdir(path)
            path = os.path.join(dir_+"/", file_[i]+"thres")
            cv2.imwrite(path+f"/{file_[i]}+thres.png", img)
            out_below = pytesseract.image_to_string(img)
            #print("out_below",  out_below)
            filesaver(path+f"/{file_[i]}+thres.txt", out_below)
            #print(path)
            cropimage, textfile = Barcode_Scanner(path_to_image=os.path.join(dir_, file_[i]))
            cv2.imwrite(path+f"/{file_[i]}+cropimg.png", cropimage)
            filesaver(path+f"/{file_[i]}+decode.txt", textfile)

            

def collectimages():
    dirname_li = []
    filenames_li = []
    for dirname, _, filenames in os.walk(os.getcwd()+'/package_images'):
        dirname_li.append(dirname)
        if '.DS_Store' in filenames:
            pass
        else:
            filenames_li.append(filenames)
       
    return dirname_li, filenames_li


if __name__ == "__main__":
    dir_, file_ = collectimages()
    #dir_.sort()
    print(dir_.remove(dir_[0]))
    print(file_)
    for i in range(0, len(file_)):
        threshold(dir_[i], file_[i])
        