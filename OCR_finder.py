import cv2
import pytesseract
from PIL import Image

def main():
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
        # Get File Name from Command Line
        path = r'D:\javascript\pp-YOLO\Work\package_images\1\01.jpeg'
        # load the image
    
        image = cv2.imread(path)
        # Convert image to grayscale
    
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        temp = input("Do you want to pre-process the image ?nThreshold : 1nGrey : 2nNone : 0nEnter your choice : ").strip()
    
         # If user enter 1, Process Threshold
        if temp == "1":
             gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        elif temp == "2":
             gray = cv2.medianBlur(gray, 3)
    
        # store grayscale image as a temp file to apply OCR
    
        filename = "{}.png".format("temp")
        
        cv2.imwrite(filename, gray)
    
        # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    
        text = pytesseract.image_to_string(Image.open(filename))
    
        print(text)

try:
     main()
except Exception as e:
     print(e.args) 
     print(e.__cause__)