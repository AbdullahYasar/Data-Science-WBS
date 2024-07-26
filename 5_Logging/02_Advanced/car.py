import logging 


logger = logging.getLogger() # get the root logger

class Car:

    def __init__(self, kz) -> None:
        self.kz =  kz
        self.color = "Red"

        logger.info("Car instance is created")
        

    def get_info(self):
        print("Ich bin ein gutes Auto")