# OCR_Recognition


:point_right: This ***ALGORITHM*** is used for the both **Optical Character Recognition** and **Barcode Detector**

## Package Images

:point_right: package image is the folder with image data 

How the images are placed in the folder

:point_right: pakage_images/foldernames ***[classes]***

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


:top_point: Above thing will give complete information how the data and the result was saved, total number of the classes in the images floders class names :point_right: **[1, 2, 3, 4, 5]**


### Barcode File 

:point_right: Barcode file is to decode barcodes

//py

    def Barcode_Scanner(path_to_image)
        return crop_ima, decode(img)

//

:point_right: Is the function which takes the image path and will return crop images **(Barcode)**, decode(image) **(decode of the barcode)**

Output of the code 

:point_right: Barcode Image

![BarCode](https://github.com/saichandrareddy1/OCR_Recognition/blob/master/package_images/5/02.jpegthres/02.jpeg%2Bcropimg.png)

Text File output [**(decode of the barcode)**](https://github.com/saichandrareddy1/OCR_Recognition/blob/master/package_images/5/02.jpegthres/02.jpeg%2Bdecode.txt)

same thing will be return to all the images in the classes


## OCR_finder file

:point_right: OCR file is used to read the text data from the image

// py 

    def filesaver(filname, text):

//