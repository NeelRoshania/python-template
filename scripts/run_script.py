import argparse
import logging

from python_template.funcs import specific_func

LOGGER = logging.getLogger(__name__) # this logger is defined seperately, see logging.conf

if __name__ == "__main__":

    LOGGER.info('testing scripted implementation')

    # parse arguments
    specific_func('Module setup! (You shouldn\'t see this log on the console)')
    

    

