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
