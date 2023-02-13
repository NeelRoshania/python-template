import logging

LOGGER = logging.getLogger(__name__) # this logger is defined seperately, see logging.conf

def specific_func(text:str) -> None:

    """
        Service to....

    """
    LOGGER.debug(text)
    # logger.debug(text)

    return None