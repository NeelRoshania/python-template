import pytest
from python_template import logger, cparser

from python_template.psql import psql_connection

# usage: 
#   - pytest tests/scripts/test_sample.py
#   - pytest -v tests/scripts/test_sample.py

def test_psqlselect():

    # setup config parser config_parser
    cparser.read('conf/pipeline.conf')

    # Test passes if connector is able to query and log the version
    logger.info(f'starting connection to psql')
    
    # establishing the connection
    conn_response = psql_connection(
        db=cparser.get('postgresql_credentials', 'database'),
        usr=cparser.get('postgresql_credentials', 'user'),        
        pswd=cparser.get('postgresql_credentials', 'password'), 
        hst=cparser.get('postgresql_credentials', 'host'), 
        prt=cparser.get('postgresql_credentials', 'port')
        )

    if conn_response["connection-status"]:

        # Creating a cursor object using the cursor() method
        conn = conn_response['conn']
        cursor = conn.cursor()

        # Executing an MYSQL function using the execute() method
        cursor.execute("select * from weather;")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchall()
        logger.info(f'data: {data}, type: {type(data)}, len: {len(data)}')

        # Closing the connection
        conn.close()
    else:
        logger.info(f'connection failed: {conn_response}')
        raise Exception(f'Failed to pass test - {conn_response}')

if __name__ == "__main__":
    test_psqlselect()
