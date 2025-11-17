import cv2

# Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load test image
image = cv2.imread("test.jpg")

if image is None:
    print("❌ Image not found! Please place 'test.jpg' here.")
else:
    print("✅ Image loaded successfully!")

# Convert to grayscale (Haar cascades require grayscale)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces 
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
