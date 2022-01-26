from hashlib import new
import logging
import csv

# setup logging environment
logger = logging.getLogger('module')

# text handling
def write_text(file_loc, data):

    try:
        with open(file_loc, "w") as f:
            f.write(data)
        logger.info(f'data written to {file_loc}')
    except Exception as e:
        logger.info(f'failed to write to {file_loc}: {e}')

def read_text(file_loc):
    try:
        with open(file_loc, "r") as f:
            _data = f.read()
        logger.info(f'data read from {file_loc}')
        return _data
    except Exception as e:
        logger.info(f'failed to read {file_loc}: {e}')

# csv handling 
def write_csv(file_loc, data):

    try:
        with open(file_loc, "w", newline='') as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerows(data)
        logger.info(f'data written to {file_loc}')
    except Exception as e:
        logger.info(f'failed to write to {file_loc}: {e}')