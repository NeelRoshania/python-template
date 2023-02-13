import argparse
import logging

from python_template import funcs

LOGGER = logging.getLogger(__name__) # this logger is defined seperately, see logging.conf

if __name__ == "__main__":

    # parse arguments
    LOGGER.info('testing scripted implementation')
    funcs.specific_func('Module setup! (You shouldn\'t see this log on the console)')
    

    

