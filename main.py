import yaml
from counters import cv2Counter

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

if sendImage:
    print(1)
else:
    print(2)

match mode:
    case 'cv2':
        counter = cv2Counter(capint,pubint,host,token,sendImage)
        counter.do()
    case 'pi':
        print(mode+" mode not implemented yet")
    case 'dev':
        print(mode+" mode not implemented yet")
    case _:
        print("Please choose an allowed mode")