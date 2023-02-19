import configparser
import logging
import logging.config

# __name__: python_template

# default log location for python_template set to python_template.log
LOGGER = logging.getLogger(__name__) # this will call logger python_template

# objects to make available when this package is imported
cparser = configparser.ConfigParser()

LOGGER.info(f'{__name__} called') # not required

# # __all__ applies to the situation where from foo.bar import *
# __all__ = [
#     'logger'
# ]