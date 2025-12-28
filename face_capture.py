import cv2
import os

name = input("Enter person name: ")

save_dir = os.path.join(os.getcwd(), "dataset", name)
os.makedirs(save_dir, exist_ok=True)

print("Saving images to:", save_dir)
print("Press 'c' to save | Press 'q' or ESC to quit")
print("IMPORTANT: CLICK on the camera window once")

cap = cv2.VideoCapture(0)
count = 0

cv2.namedWindow("Camera Test", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera error")
        break

    cv2.imshow("Camera Test", frame)

    key = cv2.waitKey(1)

    # Save image
    if key == ord('c'):
        count += 1
        img_path = os.path.join(save_dir, f"{count}.jpg")
        cv2.imwrite(img_path, frame)
        print("Saved:", img_path)

    # Quit on 'q' or ESC
    if key == ord('q') or key == 27:
        print("Quit key pressed")
        break

    # Quit if window is closed manually
    if cv2.getWindowProperty("Camera Test", cv2.WND_PROP_VISIBLE) < 1:
        print("Window closed")
        break

cap.release()
cv2.destroyAllWindows()
print("Total images saved:", count)
