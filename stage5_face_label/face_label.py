import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Replace with your DroidCam url
url = "http://192.168.00.00:4747/video"

video = cv2.VideoCapture(url)

# Temporary static label (this project does not identify real people)
label = "Known Person"

if not video.isOpened():
    print("❌ Can't open video stream!")
else:
    print("Stream started — Press 'q' to exit")

while True:
    ret, frame = video.read()
    if not ret:
        print("❌ Failed to capture frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(frame, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 255, 255), 2)

    cv2.imshow("Face Labeling Demo", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
