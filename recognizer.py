import os
import cv2
import numpy as np
from embeddings import extract_features

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def load_known_faces(dataset_path="dataset"):
    features = []
    labels = []

    for person in os.listdir(dataset_path):
        person_path = os.path.join(dataset_path, person)
        if not os.path.isdir(person_path):
            continue

        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)
            img = cv2.imread(img_path)
            if img is None:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) == 0:
                continue

            x, y, w, h = faces[0]
            face_img = img[y:y+h, x:x+w]

            feature = extract_features(face_img)
            features.append(feature)
            labels.append(person)

    return np.array(features), np.array(labels)
