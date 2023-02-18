import logging

# __name__: python_template.funcs
logging.config.fileConfig('conf/logging.conf', defaults={'fileHandlerLog': f'logs/{__name__}.log'})
LOGGER = logging.getLogger(__name__) # this will call the logger python_template.funcs

def specific_func(text:str) -> None:

    """
        Service to....

    """

    LOGGER.debug(f'{__name__} - {text}')

    return None