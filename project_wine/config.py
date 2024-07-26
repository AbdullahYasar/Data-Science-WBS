
import os 
from pathlib import Path 
import json
import logging 
from logging.config import fileConfig


os.chdir(Path(__file__).parent)


fileConfig("./config/logging.ini")

logger = logging.getLogger()

logger.info("Application Template is started!")




with open("./config/config.json", mode = "r", encoding= "UTF-8") as file:
    config_data = json.load(file)
    logger.debug(f"Configuration file is loaded")





APP_TITLE = config_data["app_title"]
APP_VERSION = config_data["app_version"]

DATA_PATH = "./data/testfile.csv"