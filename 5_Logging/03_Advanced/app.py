import os 
from pathlib import Path 
import logging 
from logging.config import fileConfig
 

os.chdir(Path(__file__).parent)


fileConfig("logging.ini")

logger = logging.getLogger()


logger.info("Application Advanced is started!")

logger.debug("Test Message")
logger.warning("Test2 Message")


logger.info("Application Advanced is finished!")