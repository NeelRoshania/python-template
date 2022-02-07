#!/bin/bash

# Sources
#   - tutorial: https://linuxconfig.org/bash-scripting-tutorial-for-beginners
#   - glossary: https://ss64.com/bash/

#
# send data to s3
#

# variable assignments
pages=data/pages
responses=data/responses
date_now=$(date +%Y-%m-%d\ %H\:%M\:%S)
backup_file=$output/$(date +%Y-%m-%d_%H%M%S)_backup.tar.gz
logs=logs

# creating log files
echo "$date_now:request_parser.sh:run starting"

# run nejm.py - get and parse requests
python scripts/nejm.py 2>> $logs/request_parser_errors.log

# export data to aws
echo "$date_now:request_parser.sh:exporting logs to s3"
aws s3 cp $logs s3://medjobs/logs/ --recursive --exclude "*.keep" 2>> $logs/request_parser_errors.log

echo "$date_now:request_parser.sh:exporting pages to s3"
aws s3 cp $pages s3://medjobs/data/pages --recursive --exclude "test_*.csv" 2>> $logs/request_parser_errors.log

echo "$date_now:request_parser.sh:exporting responses to s3"
aws s3 cp $responses s3://medjobs/data/responses --recursive --exclude "test_*.txt" 2>> $logs/request_parser_errors.log

# delete pages and responses that do not contain 'test'
cd data/pages
ls -1 | grep -v 'test' | xargs rm -f
cd ..
cd responses
ls -1 | grep -v 'test' | xargs rm -f
echo "$date_now:request_parser.sh:run complete"

