from .baseCounter import baseCounter
from ultralytics import YOLO
import cv2
import requests
import json
import time
import base64

class cv2Counter(baseCounter):

    def __init__(self, capint = 4, pubint = 60, host = None, token = None, sendImage = False) -> None:
        super(cv2Counter, self).__init__(capint,pubint,host,token,sendImage)
        self.model = YOLO("yolov8x.pt")
        self.cam = cv2.VideoCapture(0)
    
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

            ret, buffer = cv2.imencode('.jpg', self.frame)
            image_base64 = base64.b64encode(buffer)
            print(f'Mean of predicted people in the last {self.imgMax} images is {cntMean}')
            
            ts = round(time.time_ns()/1e6)
            if (self.sendImage):
                pic = "data:image/jpeg;base64,"+image_base64.decode('ascii')
                dados = {"ts": ts, "values": {"cnt": cntMean, "pic": pic}}
            else:
                dados = {"ts": ts, "values": {"cnt": cntMean}}
            
            urlPost = f'http://{self.host}/api/v1/{self.accessToken}/telemetry'
            try:
                ret = requests.post(urlPost,data=json.dumps(dados))
                if ret.status_code != 200:
                    print(ret.status_code)
                    print(ret.headers)
            except Exception as e:
                print("Cannot send data")
                print(e)

            self.predictions = [] # resets predicted array