import cv2
from cv2 import imwrite, imshow
import numpy as np
import easyocr
class screenShootProcess:
    def __init__(self, camera, image):
        pass

    def takeScreenshoot(self, camera):
        ret, image = camera.read() 
        imshow('window',image)
        imwrite('screenshoots/window.png', image)
        self.process_image(camera, image)

    def process_image(self, camera, image):
        reader = easyocr.Reader(["ru","rs_cyrillic","be","bg","uk","mn","en"])  # List of target languages
        blur = cv2.GaussianBlur(image,(5,5),0)
        Sharpeningkernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
        sharpened_image = cv2.filter2D(image, -1, Sharpeningkernel) 
        res = reader.readtext(sharpened_image, detail=0)
        text = ' '.join(res)
        print(text)

        self.drawResultToScreen(text)
        # cv2.destroyWindow('window')

    def drawResultToScreen(self,text):
        ret, self.frame = self.camera.read()

        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 255, 255)
        thickness = 2

        cv2.putText(self.frame, text, (30, 40), font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow("Look Translate", self.camera)


