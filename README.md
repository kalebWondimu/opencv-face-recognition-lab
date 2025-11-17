    opencv-face-recognition-lab

Step-by-step face recognition and computer vision project (image loading → live detection → phone integration → recognition)

A beginner-friendly, progressive mini-project collection for learning computer vision.

This repository contains Stage 1 to Stage 5 practical exercises that gradually teach OpenCV fundamentals — from loading images to real-time detection and basic labeling.

Each stage is simple, clear, and ready to run.

#Installation Guide
1. Install Python

Make sure you have Python 3.8 or newer installed.
 - python3 --version
2. Create a Virtual Environment

 -python3 -m venv cvenv
 -source cvenv/bin/activate
3. Install OpenCV and required libraries
  pip install opencv-python
  pip install numpy

->No additional installations are required for Stages 1–5.
tage Explanations

#Stage Explanations
Stage 1 — Load and Display an Image
Covers the basics of OpenCV:
  -Load an image using cv2.imread()
  -Display the image using cv2.imshow()
  -Wait for a key press and close windows
  -This is the foundation of all OpenCV projects.

Stage 2 — Face Detection on a Static Image
Introduces classical computer vision:
  -Convert images to grayscale
  -Use Haar Cascade (frontal face detector)
  -Detect faces using detectMultiScale()
  -Draw rectangles around detected faces

Stage 3 — Live Face Detection Using a Webcam
Real-time video processing:
  -Access webcam with VideoCapture(0)
  -Process frames inside a loop
  -Detect faces continuously
  -Close the window with the 'q' key

Stage 4 — Live Face Detection Using Your Phone Camera
Uses the DroidCam app to replace your webcam.

  Steps:
1. Install DroidCam on your Android phone
2. Connect via USB tethering or hotspot
3. Open DroidCam and copy the video URL (example: http://192.168.1.10:4747/video)
4. Use OpenCV to read the phone camera stream

Result: higher-quality real-time face detection.

Stage 5 — Manual Face Labeling
This stage introduces:
  -Drawing text with cv2.putText()
  -Assigning names above detected faces
  -Basic "simulated recognition" (not real AI yet)
    
    Future Stages (Coming Soon)
Stage 6 — Real Face Recognition (Using face_recognition library)
Stage 7 — Multi-person Dorm Guard System
Stage 8 — Employee Biometric Attendance System (IoT + Database)

These advanced stages will be added after the fundamentals.























