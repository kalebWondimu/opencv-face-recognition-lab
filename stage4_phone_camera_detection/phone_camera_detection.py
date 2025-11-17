import cv2

# Replace with your DroidCam URL
url = "http://192.168.000.00:4747/video"

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

video = cv2.VideoCapture(url)

if not video.isOpened():
    print("❌ Can't open phone camera. Check your WiFi connection.")
else:
    print("📱 Phone camera stream started — Press 'q' to exit")

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to retrieve frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow("Phone Camera Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
