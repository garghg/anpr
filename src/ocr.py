from skimage.metrics import structural_similarity as ssim
import os
import cv2
import easyocr

# Specify the path to the folder containing images
folder_path = "results"

# Set the threshold for considering images as duplicates
similarity_threshold = 0.9

def compare_images(imageA, imageB):
    # compute the structural similarity index for the images
    s = ssim(imageA, imageB)
    return s

def delete_duplicates(folder_path, threshold):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]

    # Loop through each pair of images
    for i, file1 in enumerate(image_files):
        for j, file2 in enumerate(image_files):
            if i < j:
                # Read and convert images to grayscale, and check if they are empty
                imageA = cv2.imread(os.path.join(folder_path, file1))
                imageB = cv2.imread(os.path.join(folder_path, file2))

                if imageA is None or imageB is None:
                    print(f"Couldn't load images: {file1}, {file2}")
                    continue

                grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
                grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

                # Compare images
                similarity = compare_images(grayA, grayB)

                # If similarity is above the threshold, delete the duplicate image
                if similarity > threshold:
                    os.remove(os.path.join(folder_path, file2))
                    print(f"Deleted {file2} (SSIM: {similarity:.2f})")


import csv

def ocr(folder):
    image_files = [f for f in os.listdir(folder) if f.lower().endswith('.jpg')]
    image_files.sort()

    # List to store results
    results = []

    # Set to store unique plates
    unique_plates = set()

    for file in image_files:
        img_path = os.path.join(folder, file)
        print(img_path)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Couldn't load image: {img_path}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        reader = easyocr.Reader(['en'])
        result = reader.readtext(gray)

        if result:
            plate = result[0][1]
            # Check if the plate is unique
            if plate not in unique_plates:
                unique_plates.add(plate)
                results.append({'Image': file, 'Plate': plate})

    # Write results to CSV file
    output_csv_path = 'output.csv'
    with open(output_csv_path, 'w', newline='') as csvfile:
        fieldnames = ['Image', 'Plate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data
        for result in results:
            writer.writerow(result)

    print(f"Results written to {output_csv_path}")

def final():
    # Delete duplicate images
    delete_duplicates(folder_path, similarity_threshold)

    # Finally, call ocr on the interested images
    ocr(folder_path)
