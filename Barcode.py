# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2
from pyzbar.pyzbar import decode
from PIL import Image

def Barcode_Scanner(path_to_image):
	# load the image and convert it to grayscale
	image = cv2.imread(path_to_image)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# compute the Scharr gradient magnitude representation of the images
	# in both the x and y direction using OpenCV 2.4
	ddepth = cv2.CV_32F if imutils.is_cv2() else cv2.CV_32F
	gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
	gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)

	# subtract the y-gradient from the x-gradient
	gradient = cv2.subtract(gradX, gradY)
	gradient = cv2.convertScaleAbs(gradient)

	# blur and threshold the image
	blurred = cv2.blur(gradient, (9, 9))
	(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

	# construct a closing kernel and apply it to the thresholded image
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
	closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

	# perform a series of erosions and dilations
	closed = cv2.erode(closed, None, iterations = 1)
	closed = cv2.dilate(closed, None, iterations = 1)

	# find the contours in the thresholded image, then sort the contours
	# by their area, keeping only the largest one
	cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]

	# compute the rotated bounding box of the largest contour
	rect = cv2.minAreaRect(c)
	box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
	box = np.int0(box)

	# draw a bounding box arounded the detected barcode and display the
	min_y = int(np.min(box[:,-1]))
	max_y = int(np.max(box[:,-1]))
	min_x = int(np.min(box[:,0]))
	max_x = int(np.max(box[:,0]))
	crop_ima = image[min_y:max_y, min_x:max_x]

	# save cropped image
	#cv2.imwrite("cropped.jpg", crop_ima)
	sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
	sharpen = cv2.filter2D(crop_ima, -1, sharpen_kernel)
	col = cv2.cvtColor(sharpen, cv2.COLOR_RGB2GRAY)
	thres, im_bw = cv2.threshold(col, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	gray = cv2.bitwise_not(im_bw)
	kernel = np.ones((2, 1), np.uint8)
	img = cv2.erode(gray, kernel, iterations=2)
	img = cv2.dilate(img, kernel, iterations=2)
	print("decoding", decode(img))
	# draw a bounding box arounded the detected barcode and display the
	# image
	cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
	#cv2.imshow("Image", im_bw)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return crop_ima, decode(img)
