from ultralytics import YOLO
import cv2
import schedule
import yaml
import requests
import json
import time

class Counter():

    def __init__(self,capint = 4, pubint = 60, host = None, token = None) -> None:
        self.model = YOLO("yolov8x.pt")
        self.cam = cv2.VideoCapture(0)
        self.frame =  None
        self.predictions = []
        self.captureInterval = capint # interval in seconds to capture images
        self.publishInterval = pubint # interval in seconds to publish human detection
        self.imgMax = self.publishInterval/self.captureInterval
        self.host = host
        self.accessToken = token

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
        cv2.imwrite("image.png", self.frame)

    def countPeople(self) -> None:
        results = self.model("image.png", classes=0, conf=0.4, verbose=False) # predict humans on image with minimum confidence of 0.4
        for result in results:
            cnt = result.boxes.cls.tolist().count(0)
            self.predictions.append(cnt)

    def sendCount(self) -> None:
        if (len(self.predictions) == self.imgMax): # checks if there is enough samples to calculate mean
            cntMean = round(sum(self.predictions)/len(self.predictions))
            print(f'Mean of predicted people in the last {self.imgMax} images is {cntMean}')
            
            ts = round(time.time_ns()/1e6)
            dados = {"ts": ts, "values": {"cnt":cntMean}}
            urlPost = f'http://{self.host}/api/v1/{self.accessToken}/telemetry'
            requests.post(urlPost,data=json.dumps(dados))

            self.predictions = [] # resets predicted array
 
try:
    with open(f'conf/config.yaml','r') as f:
        config = yaml.safe_load(f)
        capint = config["captureInterval"]
        pubint = config["publishInterval"]
        host = config["tbHost"]
        token = config["accToken"]
except FileNotFoundError:
    print("Please provide the config.yaml file")
except KeyError:
    print("Configuration error, please check config.yaml file")

counter = Counter(capint,pubint,host,token)
counter.do()