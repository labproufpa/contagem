import yaml
from counters import cv2Counter

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

counter = cv2Counter(capint,pubint,host,token)
counter.do()