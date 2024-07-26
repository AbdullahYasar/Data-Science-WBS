import os 
from pathlib import Path 
import logging 
from car import Car

os.chdir(Path(__file__).parent)


# Create/Config the logger
logger = logging.getLogger()  # get the root logger
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s  - %(filename)s - %(name)s - %(levelname)s - %(message)s ")



# File hanlder --> Messages will be saved in a file
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)


# Stream Handler --> Messages will be shown in Terminal
stream_handler = logging.StreamHandler() 
stream_handler.setFormatter(formatter)



# Add handlers to root logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)





logger.info("Application is started")

vw = Car("A1234")




logger.info("Application is finished")