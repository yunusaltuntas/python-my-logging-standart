from logging.handlers import RotatingFileHandler
from datetime import datetime
import logging
import time
import os, os.path

project_name= "project name"


def get_logger():
    if not os.path.exists("logs/"):
        os.makedirs("logs/")
    now = datetime.now()
    file_name = now.strftime(project_name + '-%H-%M-%d-%m-%Y.log')
    log_handler = RotatingFileHandler('logs/'+file_name,mode='a', maxBytes=10000000, backupCount=50)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(message)s  ', '%d-%b-%y %H:%M:%S')

    formatter.converter = time.gmtime
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    if (logger.hasHandlers()):
        logger.handlers.clear()
    logger.addHandler(log_handler)
    return logger

def main():
    logger = get_logger()

    while True:
        logger.info("information of code stream")
        logger.error("exception and other error")


if __name__ == '__main__':
    main()
