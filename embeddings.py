import cv2
import numpy as np

def extract_features(face_img):
    face_img = cv2.resize(face_img, (100, 100))
    gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

    # Histogram of pixel intensities (much more stable)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist = cv2.normalize(hist, hist).flatten()

    return hist
