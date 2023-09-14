import logging

# __name__: python_template.funcs

LOGGER = logging.getLogger(__name__) # this will call the logger python_template.funcs

# basic generator definition
def gen(l):
    """
     - equivalent to (_l for _l in l)
     - https://realpython.com/introduction-to-python-generators/
    """
    for _l in l:
        yield _l

def specific_func(text:str) -> None:

    """
        Service to....

    """

    LOGGER.info(f'starting some function.')

    return None
