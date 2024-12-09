from cv2 import imread, imshow, imwrite
import pytesseract
from PIL import ImageGrab


class screenShootProcess:
    sc_count = 1
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    def takeScreenshoot(self, camera):
        image = camera.read()
        imshow('window',image)
        imwrite('screenshoot_1.png', image)

        self.process_image(camera, image)

    def process_image(self, camera, image):
        image = ImageGrab.grab()

        # Algorithm to enhance image and to show it more clear

        text = pytesseract.image_to_string(image)
        print(text)
        
