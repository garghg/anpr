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
