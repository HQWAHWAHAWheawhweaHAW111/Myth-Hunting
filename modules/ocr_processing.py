import pytesseract
import cv2

def extract_text(image_path="screen.png"):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()

if __name__ == "__main__":
    print("Extracted text:", extract_text())
