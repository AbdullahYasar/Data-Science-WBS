
import os 
from pathlib import Path 
import logging 

os.chdir(Path(__file__).parent)


# Create/Config Logging
logging.basicConfig(filename="app.log", level = logging.DEBUG,
                    format = "%(asctime)s  - %(filename)s - %(name)s - %(levelname)s - %(message)s ")


def add(x, y):

    logging.debug(f"X: {x}, Y:{y}")    
    total = x + y
    
    
    total = round(total, 2)
    
    logging.debug(f"Total : {total}")
    return total 


def main():
    logging.info("Application is started.")
    
    total = add(6,9)

    print(f"The main total is: {total}")

    logging.info("Application is finished.")



if __name__ == "__main__":
    main()

    # logging.debug("This is a message")
    # logging.info("This is a message")
    # logging.warning("This is a message")
    # logging.error("This is a message")
    # logging.critical("This is a message")