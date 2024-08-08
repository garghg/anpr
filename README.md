# Real-time Automatic Number Plate Recognition (ANPR)
The ANPR (Automatic Number Plate Recognition) Application is a powerful and efficient tool designed to recognize and extract vehicle license plate numbers from real-time video streams. My application here uses a camera to detect, capture, and save license plates from real-time video, and then applies Optical Character Recognition (OCR) to those captured images to effectively and quickly acquire the license plate numbers.

```mermaid
flowchart TD
    A[Start] --> B[Initialize Video Capture]
    B --> C{Main Loop}
    C -->|Frame Read| D[Convert Frame to Grayscale]
    D --> E[Detect Number Plates]
    E -->|For Each Plate| F{Check Area > Min Area}
    F -->|Yes| G[Draw Rectangle and Label]
    G --> H[Extract and Resize ROI]
    H --> I[Save Resized Image]
    F -->|No| C
    I --> C
    C -->|Esc Pressed| J[Release Resources]
    J --> K[Call final() Function]
    K --> L[Delete Duplicate Images]
    L --> M[Perform OCR]
    M --> N[Save Results to CSV]
    N --> O[End]
```

## Files
### Number_plate_detection.py
Uses camera to capture video, detect license plates in the video, and save images of detected license plates in "results" folder. 

### ocr.py
Uses saved images from Number_plate_detection.py and extracts license plate numbers from those images using Optical Character Recognition or OCR, and save license plate numbers in a csv file called "output".

## Dependencies
-   haarcascade_russian_plate_number XML file _(provided)_
-   python 3.11.5 or above
-   OpenCV or cv2
-   scikit-image or skimage
-   easyocr

## Reference:
1. License plates detection logic is based on  [thesachinshakya's License Plate Detection Model](https://github.com/thesachinshakya/Number_Plate_Detection).
2. Optical Character Recognition the is applied to detected license plates is inspired by [PyImagesearch's OCR detection](https://pyimagesearch.com/2014/09/15/python-compare-two-images/).
