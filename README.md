# OCR_Recognition


:point_right: This ***ALGORITHM*** is used for the both **Optical Character Recognition** and **Barcode Detector**

## Package Images

:point_right: package image is the folder with image data 

How the images are placed in the folder

:point_right: pakage_images/foldernames ***[classes]***

```py
    # Class 1
    1/01.jpegthres/                   // Result folder
        01.jpegthres+cropimg.png
        01.jpegthres+decode.txt
        01.jpegthres+thres.png
        01.jpegthres+thres.txt
     2.jpegthres/                     // Result folder
        2.jpegthres+cropimg.png
        2.jpegthres+decode.txt
        2.jpegthres+thres.png
        2.jpegthres+thres.txt
     03.jpegthres/                    // Result folder
        03.jpegthres+cropimg.png
        03.jpegthres+decode.txt
        03.jpegthres+thres.png
        03.jpegthres+thres.txt

     01.jpeg
     2.jpeg
     03.jpeg

    # Class 2
     2/ .
        .
        .
        .
        .
    
    #Class 3
     3/ .
        .
        .
        .
        .
    # Continue to Class 4 and 5

```

:point_up: Above thing will give complete information how the data and the result was saved, total number of the classes in the images floders class names :point_right: **[1, 2, 3, 4, 5]**


### ![Barcode File](https://github.com/saichandrareddy1/OCR_Recognition/blob/master/Barcode.py)

:point_right: Barcode file is to decode barcodes

```py

    def Barcode_Scanner(path_to_image)
        return crop_ima, decode(img)
```

:point_right: Is the function which takes the image path and will return crop images **(Barcode)**, decode(image) **(decode of the barcode)**

Output of the code 

:point_right: Barcode Image

![BarCode](https://github.com/saichandrareddy1/OCR_Recognition/blob/master/package_images/5/02.jpegthres/02.jpeg%2Bcropimg.png)

Text File output [**(decode of the barcode)**](https://github.com/saichandrareddy1/OCR_Recognition/blob/master/package_images/5/02.jpegthres/02.jpeg%2Bdecode.txt)

same thing will be return to all the images in the classes


## ![OCR_finder file](https://github.com/saichandrareddy1/OCR_Recognition/blob/master/OCR_finder.py)

:point_right: OCR file is used to read the text data from the image

```python 

    def filesaver(filname, text):
        # Will save text file in target folder  

```

```py
    
    def gray(img):
        # Will return the gray Image

```

```py

    def blur(img) 
    # will return blur image

```

```py 

    def threshold(dir_, file_, total)
    ''' threshold will take three files
            1. dir id about path to root directory
            2. files name of the file it may be image or text
            3. total is the full path for the image '''
    
```

```py

    def collectimages():

        # Will collect all the images from the folders

        return dirname_li, filenames_li, total_path

        # Will retunn all the folders, images, fullpath 

```

## Algotithm Steps

1. Collecting Image
2. Making Threshold or Gray, Blur
3. Passing into the Pytessaract function
4. Create folder for the result
5. Extracting text data from the image
6. Saving text data 
7. passing data into the barcode function 
8. Crop barcode from the image
9. Decode the image
10. Save it into the folder
11. Check the pakage_image folder ***Done*** 


## Thanks 