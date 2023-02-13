import argparse
import logging

from python_template.funcs import specific_func

LOGGER = logging.getLogger(__name__) # this logger is defined seperately, see logging.conf

if __name__ == "__main__":

    LOGGER.info('testing scripted implementation')

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, action="store", default="conf/config.yaml", nargs="?")
    parser.add_argument("--optional", "-o", action="store", type=str, default=8000)
    args = parser.parse_args()

    specific_func(f'Module setup! (You shouldn\'t see this log on the console) - args:{args}')
    

    

