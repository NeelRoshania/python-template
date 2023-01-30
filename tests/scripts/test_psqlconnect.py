import pytest
from python_template import logger, cparser

from python_template.db import psql_connection

# usage: 
#   - pytest tests/scripts/test_sample.py
#   - pytest -v

# object extracts all jobs found in joblist
def test_psqlconnection():

    # setup config parser config_parser
    cparser.read('conf/pipeline.conf')

    # Test passes if connector is able to query and log the version
    logger.info(f'starting connection to psql')
    
    pswd = cparser.get('postgresql_credentials', 'password') 
    hst = cparser.get('postgresql_credentials', 'host') # this doesn't work as an argument
    prt = cparser.get('postgresql_credentials', 'port')
    
    # establishing the connection
    conn = psql_connection(
        pswd=pswd, 
        hst='127.0.0.1', 
        prt=prt
        )

    if conn["connection-status"]:

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Executing an MYSQL function using the execute() method
        cursor.execute("select version()")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        logger.info("Connection established to: ", data)

        # Closing the connection
        conn.close()
    else:
        logger.info(f'connection failed: {conn}')
        raise Exception(f'Failed to pass test - {conn}')

if __name__ == "__main__":
    test_psqlconnection()