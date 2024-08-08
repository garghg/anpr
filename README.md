# Real-time Automatic Number Plate Recognition (ANPR)
The ANPR (Automatic Number Plate Recognition) Application is a powerful and efficient tool designed to recognize and extract vehicle license plate numbers from real-time video streams. My application here uses a camera to detect and capture license plates in real-time video, and then applies Optical Character Recognition (OCR) to those captured images to effectively and quickly acquire the license plate numbers in the captured images.

## Files
### Number_plate_detection.py
Uses camera to capture video, detect license plates in the video, and save images of detected license plates in "results" folder. 

### ocr.py
Uses saved images from Number_plate_detection.py and extracts license plate numbers from those images using Optical Character Recognition or OCR, and save license plate numbers in a csv file called "output".

## Dependencies
-   haarcascade_russian_plate_number XML file (provided)
-   python 3.11.5 or above
-   OpenCV or cv2
-   scikit-image or skimage
-   easyocr

## Reference:
1. License plates detection logic is based on  [thesachinshakya's License Plate Detection Model](https://github.com/thesachinshakya/Number_Plate_Detection).
2. Optical Character Recognition the is applied to detected license plates is inspired by [PyImagesearch's OCR detection](https://pyimagesearch.com/2014/09/15/python-compare-two-images/).
