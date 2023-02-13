import configparser
import logging
import logging.config

# module level logging destination standardized here - there could be a better way to instead of hardcoding this
logging.config.fileConfig('conf/logging.conf', defaults={'fileHandlerLog': 'logs/python_template.log'})

# objects to make available when this package is imported
cparser = configparser.ConfigParser()

# # __all__ applies to the situation where from foo.bar import *
# __all__ = [
#     'logger'
# ]