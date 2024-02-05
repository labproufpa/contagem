from .baseCounter import baseCounter
from ultralytics import YOLO
import cv2
import time

class devCounter(baseCounter):

    def __init__(self, capint = 4, pubint = 8, host = None, token = None, sendImage = False) -> None:
        super(devCounter, self).__init__(capint,pubint,host,token,sendImage)
        self.model = YOLO("yolov8x.pt")
        self.cam = cv2.VideoCapture(0)
    
    def captureImage(self) -> None:
        ret, self.frame = self.cam.read()
        cv2.imwrite("image.png", self.frame)

    def countPeople(self) -> None:
        results = self.model("image.png", classes=0, conf=0.4, show=True, verbose=False) # predict humans on image with minimum confidence of 0.4
        for result in results:
            cnt = result.boxes.cls.tolist().count(0)
            self.predictions.append(cnt)

    def sendCount(self) -> None:
        if (len(self.predictions) == self.imgMax): # checks if there is enough samples to calculate mean
            cntMean = round(sum(self.predictions)/len(self.predictions))
            print(f'Mean of predicted people in the last {self.imgMax} images is {cntMean}')
            
            ts = round(time.time_ns()/1e6)
            print(ts,cntMean)
            self.predictions = [] # resets predicted array