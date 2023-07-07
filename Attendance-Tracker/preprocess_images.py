import os
import cv2

# Constants for file directories
STUDENT_IMAGES_DIR = "student_images"
CLASS_IMAGES_DIR = "class_images"

# Constants for image preprocessing
RESIZE_WIDTH = 128
RESIZE_HEIGHT = 128
GRAYSCALE = True


def preprocess_student_images():
    # Create a directory to store preprocessed student images
    os.makedirs("preprocessed_student_images", exist_ok=True)

    # Iterate through each student image file
    for filename in os.listdir(STUDENT_IMAGES_DIR):
        # Load and preprocess each image
        image_path = os.path.join(STUDENT_IMAGES_DIR, filename)
        image = cv2.imread(image_path)

        # Resize the image
        image = cv2.resize(image, (RESIZE_WIDTH, RESIZE_HEIGHT))

        # Convert to grayscale if required
        if GRAYSCALE:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Normalize pixel values
        image = image / 255.0

        # Save the preprocessed image
        save_path = os.path.join("preprocessed_student_images", filename)
        cv2.imwrite(save_path, image)


def preprocess_class_images():
    # Create a directory to store preprocessed class images
    os.makedirs("preprocessed_class_images", exist_ok=True)

    # Iterate through each class image file
    for filename in os.listdir(CLASS_IMAGES_DIR):
        # Load and preprocess each image
        image_path = os.path.join(CLASS_IMAGES_DIR, filename)
        image = cv2.imread(image_path)

        # Resize the image
        image = cv2.resize(image, (RESIZE_WIDTH, RESIZE_HEIGHT))

        # Convert to grayscale if required
        if GRAYSCALE:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Normalize pixel values
        image = image / 255.0

        # Save the preprocessed image
        save_path = os.path.join("preprocessed_class_images", filename)
        cv2.imwrite(save_path, image)


# Call the preprocessing functions
preprocess_student_images()
preprocess_class_images()
