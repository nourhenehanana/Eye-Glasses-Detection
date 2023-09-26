from imutils import paths
import argparse
import cv2
import numpy as np
import dlib
import matplotlib.pyplot as plt
from PIL import Image
import statistics

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
ap=ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images",required=True,help="path to input directory of images")
args = vars(ap.parse_args())
#load the classifier
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#loop over the input images
S=0
for imagePath in paths.list_images(args["images"]):
    img = dlib.load_rgb_image(imagePath)
    rect = detector(img)[0]
    sp = predictor(img, rect)
    landmarks = np.array([[p.x, p.y] for p in sp.parts()])
    nose_bridge_x = []
    nose_bridge_y = []
    for i in [28,29,30,31,33,34,35]:
            nose_bridge_x.append(landmarks[i][0])
            nose_bridge_y.append(landmarks[i][1])


    ### x_min and x_max
    x_min = min(nose_bridge_x)
    x_max = max(nose_bridge_x)
    ### ymin (from top eyebrow coordinate),  ymax
    y_min = landmarks[20][1]
    y_max = landmarks[31][1]
    img2 = Image.open(imagePath)
    img2 = img2.crop((x_min,y_min,x_max,y_max))
    img_blur = cv2.GaussianBlur(np.array(img2),(3,3), sigmaX=0, sigmaY=0)
    edges = cv2.Canny(image =img_blur, threshold1=100, threshold2=200)
    edges_center = edges.T[(int(len(edges.T)/2))]
    faces=face_cascade.detectMultiScale(img)
    for (x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        if 255 in edges_center:
            text="Glasses are present"
        else:
            text="Glasses are not present"
        cv2.putText(img, "{}: {:.2f}".format(text, S), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow('image',img)
    S+=1
    cv2.waitKey()
    


