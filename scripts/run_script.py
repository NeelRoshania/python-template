import argparse
import logging
import logging.config
import configparser

if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser(description='python bioler-plate template')
    parser.add_argument('required_argument', type=str, help='required script argument')
    parser.add_argument('-opt', '--optional', default=None, help='optional script argument')
    args = parser.parse_args()

    # setup logging environment
    logging.config.fileConfig('conf/logging.conf', defaults={'fileHandlerLog': 'logs/run_script.log'})
    logger = logging.getLogger('main')

    # config_parser
    cparser = configparser.ConfigParser()
    cparser.read('conf/pipeline_hidden.conf')
    access_key = cparser.get('aws_boto_credentials', 'access_key')
    secrey_key = cparser.get('aws_boto_credentials', 'secret_key')

    # setup and run wdod
    logger.info(f'--- starting run_script ---')

    # complete script below
    logger.warning(f'args: {args}')

    # end of script
    logger.error(f'--- run_script complete ---')

    

