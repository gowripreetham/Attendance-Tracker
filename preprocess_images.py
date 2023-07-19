import os
import cv2
import numpy as np

# Constants for file directories
STUDENT_IMAGES_DIR = "student_images"
# CLASS_IMAGES_DIR = 'class_images'

# Constants for image preprocessing
RESIZE_WIDTH = 160
RESIZE_HEIGHT = 160
GRAYSCALE = True
DENOISE = True


def preprocess_student_images():
    print("Preprocessing student images...")

    # Create a directory to store preprocessed student images
    os.makedirs("preprocessed_student_images", exist_ok=True)

    # Iterate through each student image file
    for filename in os.listdir(STUDENT_IMAGES_DIR):
        # Skip non-image files
        if not any(filename.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png"]):
            continue

        # Load and preprocess each image
        image_path = os.path.join(STUDENT_IMAGES_DIR, filename)
        image = cv2.imread(image_path)

        # Verify image loading
        if image is None:
            print(f"Error loading image: {image_path}")
            continue

        # Resize the image
        image = cv2.resize(image, (RESIZE_WIDTH, RESIZE_HEIGHT))

        # Convert to grayscale if required
        if GRAYSCALE:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Denoise with Gaussian blur if required
        # if DENOISE:
        # image = cv2.GaussianBlur(image, (3, 3), 0)

        # Save the preprocessed image with the original filename
        save_path = os.path.join("preprocessed_student_images", filename)
        cv2.imwrite(save_path, image)

    print("Student image preprocessing completed.")


"""
def preprocess_class_images():
    print("Preprocessing class images...")

    # Create a directory to store preprocessed class images
    os.makedirs('preprocessed_class_images', exist_ok=True)

    # Iterate through each class image file
    for filename in os.listdir(CLASS_IMAGES_DIR):
        # Skip non-image files
        if not any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
            continue

        # Load and preprocess each image
        image_path = os.path.join(CLASS_IMAGES_DIR, filename)
        image = cv2.imread(image_path)

        # Verify image loading
        if image is None:
            print(f"Error loading image: {image_path}")
            continue

        # Resize the image
        image = cv2.resize(image, (RESIZE_WIDTH, RESIZE_HEIGHT))

        # Convert to grayscale if required
        if GRAYSCALE:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Normalize pixel values
        image = image / 255.0

        # Save the preprocessed image with the original filename
        save_path = os.path.join('preprocessed_class_images', filename)
        cv2.imwrite(save_path, image)

    print("Class image preprocessing completed.")

"""

# Call the preprocessing functions
preprocess_student_images()
# preprocess_class_images()
