import cv2
import os
import time

# Set the dataset directory and label names
dataset_dir = 'dataset'
label_names = ['Hat', 'No Hat']

# Create the dataset directory if it doesn't exist
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Set the number of images to capture per label
num_images_per_label = 25

# Capture images and save them to the dataset directory
for label_name in label_names:
    label_dir = os.path.join(dataset_dir, label_name)
    if not os.path.exists(label_dir):
        os.makedirs(label_dir)

    print(f'Capturing {num_images_per_label} images for "{label_name}"...')
    for i in range(num_images_per_label):
        ret, frame = cap.read()

        # Display the live feed
        cv2.imshow('Capturing Images', frame)
        cv2.waitKey(1)

        img_path = os.path.join(label_dir, f'{label_name}_{i+1}.jpg')
        cv2.imwrite(img_path, frame)
        print(f'Saved image {i+1}/{num_images_per_label}')

        # Wait for 1 seconds before capturing the next image
        time.sleep(1)
    time.sleep(5)
# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()