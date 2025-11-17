import cv2

# Load image (replace with your own test.jpg file)
image = cv2.imread("test.jpg")

if image is None:
    print("❌ Image not found! Please place 'test.jpg' in this folder.")
else:
    print("✅ Image loaded successfully!")

# Display the image
cv2.imshow("Test Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
