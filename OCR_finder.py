import cv2
from pytesseract import pytesseract
from PIL import Image
import numpy as np


# preprocessing
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
def threshold(img):
    #pixels with value below 100 are turned black (0) and those with higher value are turned white (255)
    images = []
    techs = [cv2.THRESH_BINARY,
        cv2.THRESH_BINARY_INV,
        cv2.THRESH_TRUNC,
        cv2.THRESH_TOZERO,
        cv2.THRESH_TOZERO_INV]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    count = 0
    for i in range(len(techs)):
         for j in range(len(techs)):
               img = cv2.threshold(img, 128, 255, techs[i] & techs[j])[1]    
               gray = cv2.bitwise_not(img)
               kernel = np.ones((2, 1), np.uint8)
               img = cv2.erode(gray, kernel, iterations=2)
               img = cv2.dilate(img, kernel, iterations=2)
               images.append(img)
               cv2.imwrite(f"images/img_threshold{count}.png",img)
               count +=1 
    return images

def new():
    img = cv2.imread('/home/saireddy/OCR/OCR_Recognition/package_images/1/2.jpeg')
    #Alternatively: can be skipped if you have a Blackwhite image
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        print("ss")
    gray, img_bin = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    gray = cv2.bitwise_not(img_bin)
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.erode(gray, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)
    out_below = pytesseract.image_to_string(img)
    print("OUTPUT:", out_below)

new()

def main():
     # read image
     im = cv2.imread('/home/saireddy/OCR/OCR_Recognition/package_images/1/2.jpeg')
     #lis = [gray(im), blur(im)]
     li = threshold(im)
     print(li)
     # configurations
     config = ('-l eng --oem 1 --psm 3')
     # pytessercat
     for i in li:
          #out_below = pytesseract.image_to_string(img)
          text = pytesseract.image_to_string(i, config=config)
          # print text
          
          text = text.split('\n')
          if len(text) > 4:
            print(len(text), text)
          else:
              pass

main()

# def main():
#         #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
#         # Get File Name from Command Line
#         path = '/home/saireddy/OCR/OCR_Recognition/package_images/1/01.jpeg'
#         # load the image
    
#         image = cv2.imread(path)
#         # Convert image to grayscale
    
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#         temp = input("Do you want to pre-process the image ?nThreshold : 1nGrey : 2nNone : 0nEnter your choice : ").strip()
    
#          # If user enter 1, Process Threshold
#         if temp == "1":
#              #gray = cv2.medianBlur(gray, 3)
#              gray = cv2.threshold(gray, 0, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)[1]
#         elif temp == "2":
#              gray = cv2.medianBlur(gray, 3)
    
#         # store grayscale image as a temp file to apply OCR
    
#         filename = "{}.png".format("temp")
        
#         cv2.imwrite(filename, gray)
    
#         # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    
#         text = pytesseract.image_to_string(Image.open(filename))
    
#         print(text)

# try:
#      main()
# except Exception as e:
#      print(e.args) 
#      print(e.__cause__)