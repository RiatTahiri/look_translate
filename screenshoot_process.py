import cv2
from cv2 import imwrite, imshow
import numpy as np
from PIL import ImageGrab
import easyocr


class screenShootProcess:
    def __init__(self, camera):
        pass

    def takeScreenshoot(self, camera):
        ret, image = camera.read() 
        imshow('window',image)
        imwrite('window.png', image)

        self.process_image(camera, image)
        # self.process_image(camera, image)

    def process_image(self, camera, image):
        reader = easyocr.Reader(["ru","rs_cyrillic","be","bg","uk","mn","en"])  # List of target languages
        blur = cv2.GaussianBlur(image,(5,5),0)
        Sharpeningkernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
        sharpened_image = cv2.filter2D(image, -1, Sharpeningkernel) 
        res = reader.readtext(sharpened_image, detail=0)
        text = ' '.join(res)
        print(text)

        cv2.destroyWindow('window')
