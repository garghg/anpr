
#Reference: https://github.com/thesachinshakya/Number_Plate_Detection

#Make changes:
    #change all file paths - DONE
    #Remove the save image when clicked "s" - DONE
    #save image when plate is detected automatically - DONE
    #only save one image per plate, not one image per frame - DONE
        #will create duplicates
        #remove duplicate plates by checking which images are too similar and deleting all except one
#Next steps:
    #get colab notebook code to a local vs code file (Reference: https://github.com/nicknochnack/ANPRwithPython)
        #already modified the code to handle multiple plates but didn't have to...:(
            #upload the modified code to GH and reference my own code? Nope.
    #hook that code with images folder
    #perform ocr using that code
    #Output
        #save images with appened boxes and license plate text on top
        #save the plates in a csv/excel/other file

import cv2
from ocr import final

frameWidth = 640    # Frame Width
frameHeight = 480   # Frame Height

plateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 500
output_dimensions = (300, 150)  # Set dimensions for the saved images (width, height)

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "NumberPlate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            imgRoi = img[y:y + h, x:x + w]

            # Resize the image to the set dimensions
            imgRoi_resized = cv2.resize(imgRoi, output_dimensions)

            # Save the resized image when a valid number plate is detected
            cv2.imwrite("C:/Users/gargh/anaconda3/envs/anpr/Results/" + str(count) + ".jpg", imgRoi_resized)
            count += 1

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit the loop
        break

cap.release()
cv2.destroyAllWindows()

final()