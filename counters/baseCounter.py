import schedule
from abc import ABC, abstractmethod 

class baseCounter(ABC):

    def __init__(self, capint = 4, pubint = 60, host = None, token = None) -> None:
        self.model = None
        self.cam = None
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

    @abstractmethod
    def captureImage(self) -> None:
        pass

    @abstractmethod
    def countPeople(self) -> None:
        pass

    @abstractmethod
    def sendCount(self) -> None:
        pass