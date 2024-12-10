import cv2
import threading
from concurrent.futures import ThreadPoolExecutor

# custom scripts
import screenshoot_process as sp

class Translate:
    def __init__(self):
        self.running = True
        self.camera = cv2.VideoCapture(0)
        self.width = 0
        self.height = 0
        self.FPS = 0
        self.sc = sp.screenShootProcess(self.camera, None)

        self.mainThread = threading.Thread(target=self.runThread)
        self.executorMain = ThreadPoolExecutor(max_workers=5)

        self.mainThread.start()

    def runThread(self):
        if(self.camera.isOpened()):
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

            while(self.running):
                ret, self.frame = self.camera.read()
                if(ret):
                    
                    try:
                        self.drawCameraInfo(self.frame, self.width, self.height, self.FPS)
                    except Exception as e:
                        print(e)

                    cv2.imshow("Look Translate", self.frame)

                    self.width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
                    self.height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
                    self.FPS = self.camera.get(cv2.CAP_PROP_FPS)
                    
                    if(cv2.waitKey(1) & 0xFF == ord('q')):
                        self.running = False

                    elif(cv2.waitKey(1) & 0xFF == ord('s')):
                        self.executorMain.submit(self.sc.takeScreenshoot, self.camera)
                else:
                    print("Cannot read the frame")
                    self.running = False
        else:
            print("Cannot open the camera")
            self.running = False

        self.camera.release()
        cv2.destroyAllWindows()

    def stopThread(self):
        self.running = False
        self.mainThread.join()
    
    def drawCameraInfo(self, frame, width, height, FPS):
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.8
        color = (255, 255, 255)
        thickness = 2

        cv2.putText(frame, f"Width: {int(width)}", (10, 30), font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.putText(frame, f"Height: {int(height)}", (10, 80), font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.putText(frame, f"FPS: {int(FPS)}", (10, 110), font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.putText(frame, f'q to exit', (10, 130), font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.putText(frame, f's to take screenshot', (10, 150), font, fontScale, color, thickness, cv2.LINE_AA)

        cv2.imshow("Look Translate", self.frame)


if __name__ == "__main__":
    try:
        translate = Translate()
        translate.mainThread.join()
    except KeyboardInterrupt:
        translate.stopThread()