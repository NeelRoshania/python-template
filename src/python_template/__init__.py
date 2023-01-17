import configparser
import logging
import logging.config

# setup
logging.config.fileConfig('conf/logging.conf', defaults={'fileHandlerLog': 'logs/python_template.log'})

# objects to make available when this package is imported
logger = logging.getLogger(__name__) # ucmerced_housing
cparser = configparser.ConfigParser()

# # __all__ applies to the situation where from foo.bar import *
# __all__ = [
#     'logger'
# ]