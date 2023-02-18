import argparse
import logging

from python_template.funcs import specific_func

def main(args):
    LOGGER = logging.getLogger(__name__) # this will call the logger __main__ which will log to that referenced in python_template.__init__

    LOGGER.info('testing scripted implementation')
    specific_func(f'Module setup! (You shouldn\'t see this log on the console) - args:{args}')

if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, action="store", default="conf/config.yaml", nargs="?")
    parser.add_argument("--optional", "-o", action="store", type=str, default=8000)
    args = parser.parse_args()

    main(args)

    
    

    

