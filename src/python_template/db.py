import psycopg2
from psycopg2 import OperationalError
def psql_connection(
    pswd: str,
    hst: str,
    prt: str,
    db: str = 'postgres',
    usr: str = 'postgres'
) -> any:
    print(f'connecting to psql {hst}:{prt}:{db}') # need to log this

    try:
        return {
            "connection-status": True,
            "conn-object": psycopg2.connect(
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
            "conn-object": None,
            "reason": oe
        }