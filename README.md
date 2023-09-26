# Eye-Glasses-Detection
This repository includes a Python script for detecting whether a person is wearing glasses in a set of input images using a combination of dlib's facial landmarks, Haar cascades for face detection, and edge detection using Canny. Here's a brief explanation of the code:

# Importing Libraries and Modules:
The script starts by importing several Python libraries and modules, including imutils, argparse, cv2 (OpenCV), numpy, dlib, matplotlib, and PIL (Python Imaging Library). These libraries are used for various image processing and computer vision tasks.

# Face Detection Setup: 
The code sets up a face detector using the Haar cascade classifier (haarcascade_frontalface_default.xml) from OpenCV and a facial landmarks detector using dlib's get_frontal_face_detector and shape_predictor with a pre-trained model (shape_predictor_68_face_landmarks.dat).

# Command Line Arguments:
The script uses the argparse library to parse command-line arguments. Specifically, it expects the user to provide the path to a directory containing input images using the -i or --images argument.


# Facial Landmark Detection: 
For each image, it loads the image and uses dlib's face detector to find the face's bounding box. It then uses the shape predictor to locate 68 facial landmarks.
1. Isolating the Region of Interest (ROI): The script extracts a region of interest (ROI) around the nose bridge area by identifying specific landmarks (e.g., nose and eyebrows) and cropping the image to include this area.

2. Image Blurring and Edge Detection: The extracted ROI is loaded as a PIL Image and then converted to a NumPy array for image processing. Gaussian blur is applied to this region, and Canny edge detection is performed to detect edges within the blurred ROI.

# Face Detection with Haar Cascade: 
The script also attempts to detect faces in the entire image using the Haar cascade classifier. If a face is detected, a blue rectangle is drawn around it.

# Glasses Detection: 
The presence of glasses is determined based on the presence of edges in the center row of the ROI obtained earlier. If there are edges (values equal to 255) in this center row, it concludes that glasses are present. Otherwise, it assumes glasses are not present.

# Displaying Results: 
The script displays the processed image with rectangles indicating detected faces and text indicating whether glasses are present. It also increments a variable S as a counter to keep track of the number of processed images.
![git2](https://github.com/nourhenehanana/Eye-Glasses-Detection/assets/93352403/a724f812-f09a-4a05-8c7b-1c9ecdcff2a8)
![git3](https://github.com/nourhenehanana/Eye-Glasses-Detection/assets/93352403/9308bbc8-af27-4ad3-870e-7a5afc0ff5c7)

