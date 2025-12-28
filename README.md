# AI-Based Smart Visitor System with Face Recognition and Instant Alerts

## 📌 Project Overview
The AI-Based Smart Visitor System is a real-time security application that identifies known and unknown visitors using face recognition. When an unknown person is detected, the system generates an instant desktop alert. The project is designed to be simple, laptop-friendly, and suitable for academic mini-project demonstrations.

---

## 🎯 Objectives
- To recognize authorized (known) visitors using face recognition
- To detect unknown visitors in real time
- To generate instant alerts only once per unknown visitor
- To avoid repeated or annoying notifications
- To provide a practical AI-based security solution

---

## 🧠 Features
- Face capture and dataset creation
- Real-time face recognition (Known / Unknown)
- Intelligent one-time alert system
- Stable alert logic using scene-lock mechanism
- Laptop camera supported
- Clean and simple user interaction

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Libraries Used:**  
  - OpenCV  
  - NumPy  
  - Plyer (for desktop notifications)

---

## 📂 Project Structure
```text
SmartVisitorSecuritySystem/
│
├── alert_desktop.py          # Desktop notification alerts
├── antispoof.py              # Anti-spoofing (fake face detection)
├── delete_dataset.py         # Delete stored face datasets
├── embeddings.py             # Face feature extraction
├── face_capture.py           # Capture face images for dataset
├── face_recognition_live.py  # Live face recognition + alerts
├── recognizer.py             # Face matching and recognition logic
│
├── dataset/                  # Face image dataset (ignored in GitHub)
│   └── .gitkeep              # Keeps empty dataset folder
│
├── requirements.txt          # Project dependencies
├── .gitignore                # Ignore venv, cache, dataset images
└── README.md                 # Project documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/SmartVisitorSecuritySystem.git
cd SmartVisitorSecuritySystem

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ How to Run the Project
Step 1: Capture face images
python face_capture.py

1.Enter your name
2.Press C to capture images
3.Capture at least 20 images
4.Press Q to quit

Step 2: Run face recognition system
python face_recognition_live.py

Press Q / ESC or close window to exit
✅ Conclusion

This project successfully demonstrates a smart and efficient visitor monitoring system using face recognition and instant alerts. It provides a strong foundation for real-time security applications and academic learning.