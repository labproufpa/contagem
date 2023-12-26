from ultralytics import YOLO
import cv2
import schedule
import os
import yaml

class Counter():

    def __init__(self,capint = 4,pubint = 60) -> None:
        self.model = YOLO("yolov8x.pt")
        self.cam = cv2.VideoCapture(0)
        self.frame =  None
        self.predictions = []
        self.captureInterval = capint # interval in seconds to capture images
        self.publishInterval = pubint # interval in seconds to publish human detection
        self.imgMax = self.publishInterval/self.captureInterval

    def process(self) -> None:
        self.captureImage()
        self.countPeople()
        self.sendCount()

    def do(self) -> None:
        schedule.every(self.captureInterval).seconds.do(self.process)
        run  = True
        try:
            while run:
                schedule.run_pending()
        except KeyboardInterrupt:
            run = False
        self.cam.release()

    def captureImage(self) -> None:
        ret, self.frame = self.cam.read()

    def countPeople(self) -> None:
        results = self.model(self.frame, classes=0, conf=0.4, verbose=False) # predict humans on image with minimum confidence of 0.4
        for result in results:
            cnt = result.boxes.cls.tolist().count(0)
            self.predictions.append(cnt)

    def sendCount(self) -> None:
        if (len(self.predictions) == self.imgMax): # if there's not enough samples to calculate mean
            cntMean = round(sum(self.predictions)/len(self.predictions))
            print(f'Mean of predicted people in the last {self.imgMax} images is {cntMean}')
            self.predictions = [] # resets predicted array
 
try:
    with open(f'config.yaml','r') as f:
        config = yaml.safe_load(f)
        capint = config["captureInterval"]
        pubint = config["publishInterval"]
    print(capint,pubint) 
except FileNotFoundError:
    print("Please provide the config.yaml file")
except KeyError:
    print("Configuration error, please check config.yaml file")

#counter = Counter()
#counter.do(capint,pubint)