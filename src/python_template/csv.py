import logging
import csv

from ucmerced_housing import logger

def write_text(file_loc: str, data: str, encoding:str = None) -> None:

    """     
        ***

        write_text(file_loc: str, data: str)  -> None
            - write string data to file

    """
    
    # handling optional arguments
    data = "" if data is None else data
    encoding = 'utf-8' if encoding is None else encoding

    try:
        with open(file_loc, "w", encoding=encoding) as f:
            f.write(data)
        logger.info(f'text data written to {file_loc}')
    except Exception as e:
        logger.debug(f'failed to write to {file_loc}: {e}')
        raise Exception(e)

def write_csv(file_loc:str, data: list, schema: list = None, encoding:str = None) -> None:

    """
        ***

        write_csv(file_loc:str, data: list) -> None
            - write comma seperated list objects

    """

    # handle optional arguments
    data = [] if data is None else data
    encoding = 'utf-8-sig' if encoding is None else encoding

    try:

        with open(file_loc, "w", newline='', encoding=encoding) as f:
            writer = csv.writer(f, delimiter=",")
            if schema is not None:
                writer.writerows(schema)
                writer.writerows(data)
            else:
                writer.writerows(data)
        logger.info(f'data written to {file_loc}, encoding: {encoding}')

    except Exception as e:
        logger.debug(f'failed to write to {file_loc}: {e}')
        raise Exception(e)

def read_text(file_loc: str, encoding:str = None) -> str:

    """
        ***

        read_text(file_loc: str) -> None
            - read text data

    """

    try:

        encoding = 'utf-8-sig' if encoding is None else encoding
        with open(file_loc, "r", encoding=encoding) as f:
            _data = f.read()
        logger.info(f'data read from {file_loc}')
    
        return _data
    
    except Exception as e:
        logger.debug(f'failed to read {file_loc}: {e}')
        raise Exception(e)
        
def read_csv(file_loc:str, encoding:str = None, delimiter:str = None) -> list:

    """
        ***

        read_csv(file_loc:str, encoding:str = None, delimiter:str = None) -> list:
            - write comma seperated list objects

    """

    # handle optional arguments
    encoding = 'utf-8-sig' if encoding is None else encoding
    delimiter = ',' if delimiter is None else delimiter
    _data = []

    try:
        
        # read csv and return list data object
        with open(file_loc, newline='', encoding=encoding) as f:
            reader = csv.reader(f, delimiter=delimiter)
            for row in reader:
                _data.append(row)
 
        logger.info(f'data read from {file_loc}, encoding: {"defualt" if encoding is None else encoding}, delimiter: {delimiter}')
        
        return _data
    
    except Exception as e:
        logger.debug(f'failed to read csv from {file_loc}: {e}')
        raise Exception(e)