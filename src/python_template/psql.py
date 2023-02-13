import psycopg2

from python_template import logger
from psycopg2 import OperationalError

def psql_connection(
    db: str,
    usr: str,    
    pswd: str,
    hst: str,
    prt: str
) -> any:
    logger.info(f'connecting to psql {hst}:{prt}:{db}') # need to log this

    try:
        return {
            "connection-status": True,
            "conn": psycopg2.connect(
                                                database=db, 
                                                user=usr, 
                                                password=pswd, 
                                                host=hst, 
                                                port=prt
                                            )
        }
    except OperationalError as oe:
        return {
            "connection-status": False,
            "conn": None,
            "reason": oe
        }