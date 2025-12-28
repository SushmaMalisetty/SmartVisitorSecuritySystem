# antispoof.py

import cv2
import numpy as np

class AntiSpoof:
    def __init__(self):
        self.prev_gray = None
        self.motion_threshold = 2.0  # you can tune this

    def is_real_face(self, face_img):
        # Force same size every time
        face_img = cv2.resize(face_img, (100, 100))

        gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        if self.prev_gray is None:
            self.prev_gray = gray
            return True  # assume real for first frame

        # Now sizes ALWAYS match
        diff = cv2.absdiff(self.prev_gray, gray)
        motion_score = np.mean(diff)

        self.prev_gray = gray

        # Low motion → spoof
        if motion_score < self.motion_threshold:
            return False

        return True
