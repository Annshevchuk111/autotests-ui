import logging
import sys


def get_logger(name:str) -> logging.Logger:
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler=logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter=logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

logger=get_logger('Page')
logger.info("This is a info message")
logger.warning("This is a warning message")