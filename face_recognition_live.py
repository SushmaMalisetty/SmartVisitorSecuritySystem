import cv2
import numpy as np
from recognizer import load_known_faces
from embeddings import extract_features
from alert_desktop import send_desktop_alert

def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load known faces
known_features, known_labels = load_known_faces()
if len(known_features) == 0:
    print("No dataset found.")
    exit()

# 🔐 ALERT LOCK (defined BEFORE loop)
scene_locked = False

cap = cv2.VideoCapture(0)
cv2.namedWindow("Smart Visitor System", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Smart Visitor System", 900, 650)

THRESHOLD = 0.70
print("Press Q or ESC to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    known_present = False
    unknown_present = False

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]

        feature = extract_features(face_img)
        scores = [cosine_sim(feature, f) for f in known_features]

        best_score = max(scores)
        best_idx = np.argmax(scores)

        if best_score >= THRESHOLD:
            known_present = True
            name = known_labels[best_idx]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, name, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        else:
            unknown_present = True
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
            cv2.putText(frame, "Unknown", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

    # 🔔 ALERT LOGIC (ONE TIME ONLY)
    if unknown_present and not known_present and not scene_locked:
        send_desktop_alert("Unknown visitor detected!")
        scene_locked = True

    # 🔓 Reset lock when scene is empty or owner appears
    if known_present or len(faces) == 0:
        scene_locked = False

    cv2.imshow("Smart Visitor System", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

    # Quit if window is closed
    if cv2.getWindowProperty("Smart Visitor System", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
