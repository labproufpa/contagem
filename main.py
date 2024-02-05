import yaml
from counters import cv2Counter, devCounter, piCounter

try:
    with open(f'conf/config.yaml','r') as f:
        config = yaml.safe_load(f)
        capint = config["captureInterval"]
        pubint = config["publishInterval"]
        host = config["tbHost"]
        token = config["accToken"]
        mode = config["mode"]
        sendImage = config["sendImage"]
except FileNotFoundError:
    print("Please provide the config.yaml file")
except KeyError:
    print("Configuration error, please check config.yaml file")

if mode == 'cv2':
    counter = cv2Counter(capint,pubint,host,token,sendImage)
    counter.do()
elif mode == 'pi':
    print(mode+" mode not implemented yet")
elif mode == 'dev':
    print("Started development mode")
    counter = devCounter()
    counter.do()
else:
    print("Please choose an allowed mode")