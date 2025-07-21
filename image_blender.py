# -*- coding: utf-8 -*-
"""
Blends two images using a weighted sum with OpenCV.

This script loads two input images and combines them into a single image
using the cv2.addWeighted() function. This creates a blending or
superposition effect with adjustable transparency levels.

Dependencies:
    - opencv-python
    - numpy

Usage:
    1. Save this script in a folder.
    2. Place the two input images ('image1.jpg' and 'image2.jpg')
       in the same folder.
    3. Run the script. The result will be saved as 'blended_image.jpg'
       in a new subfolder named 'results/'.
"""

import cv2
import os

# --- CONFIGURATION ---
# Use relative paths for portability.
IMAGE1_PATH = 'image1.jpg'
IMAGE2_PATH = 'image2.jpg'
OUTPUT_FOLDER = 'results'

# Create the output folder if it doesn't exist.
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
    print(f"Created directory: {OUTPUT_FOLDER}")

# Verify that the input image files exist.
if not os.path.isfile(IMAGE1_PATH) or not os.path.isfile(IMAGE2_PATH):
    print(f"Error: Make sure '{IMAGE1_PATH}' and '{IMAGE2_PATH}' exist in the directory.")
    exit()

# Load the images from the files.
image1 = cv2.imread(IMAGE1_PATH)
image2 = cv2.imread(IMAGE2_PATH)

# Verify that the images were loaded correctly.
if image1 is None or image2 is None:
    print("Error: Could not load one or both images. Check the files.")
    exit()

# Ensure both images have the same dimensions to perform operations.
# We resize image1 to match the dimensions of image2.
if image1.shape != image2.shape:
    print("Images have different sizes. Resizing image 1...")
    image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

# --- BLENDING LOGIC ---

# Define the weights for the blend. The sum of alpha and beta is usually 1.0.
# The formula is: result = image1 * alpha + image2 * beta + gamma
alpha = 0.7  # Weight or "visibility" of the first image.
beta = 0.3   # Weight or "visibility" of the second image.
gamma = 0    # Scalar value added to each pixel sum (usually 0).

print(f"Blending images with a weight of {alpha*100}% for the first and {beta*100}% for the second.")

# Apply the weighted sum to blend the images.
blended_image = cv2.addWeighted(image1, alpha, image2, beta, gamma)

# Save the resulting image.
output_path = os.path.join(OUTPUT_FOLDER, 'blended_image.jpg')
cv2.imwrite(output_path, blended_image)
print(f"Blended image saved successfully at: {output_path}")

# Display the final result.
cv2.imshow('Blended Image', blended_image)

# Wait for the user to press a key to close the window.
print("Press any key to close the window.")
cv2.waitKey(0)
cv2.destroyAllWindows()