import cv2

class Translate:
    def __init__(self):
        
        running = True
        camera = cv2.VideoCapture(0)
        self.width = 0
        self.height = 0
        self.FPS = 0

        if(camera.isOpened()):
            while(running):
                ret, self.frame = camera.read()

                if(ret):
                    self.drawCameraInfo(self.frame, self.width, self.height, self.FPS)

                    cv2.imshow("Look Translate", self.frame)

                    self.width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
                    self.height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
                    self.FPS = camera.get(cv2.CAP_PROP_FPS)
                    if(cv2.waitKey(1) & 0xFF == ord('q')):
                        running = False
                else:
                    print("Cannot read the frame")
                    running = False
        else:
            print("Cannot open the camera")
            running = False

        
        camera.release()
        cv2.destroyAllWindows()
    
    def drawCameraInfo(self, frame, width, height, FPS):

        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (255, 255, 255)
        thickness = 1

        cv2.putText(frame, f"Width: {int(width)}", (10, 30), font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.putText(frame, f"Height: {int(height)}", (10, 60), font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.putText(frame, f"FPS: {int(FPS)}", (10, 90), font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.putText(frame, f'q to exit', (10, 120), font, fontScale, color, thickness, cv2.LINE_AA)

        cv2.imshow("Look Translate", self.frame)
    
    def translateRequest(self, word):
        pass


translate = Translate()