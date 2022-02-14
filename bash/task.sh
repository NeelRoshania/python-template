#!/bin/bash

# Sources
#   - tutorial: https://linuxconfig.org/bash-scripting-tutorial-for-beginners
#   - glossary: https://ss64.com/bash/

#
# sample execution - create a backup of scripts
#

# variable assignments
input=scripts/tools
output=bash/output
backup_file=$output/$(date +%Y-%m-%d_%H%M%S)_backup.tar.gz
aws_arn="${ENV_VAR:-ENVNOTSET}" # defualt to value if env not found

# functional assignments
function total_files {
        find $1 -type f | wc -l
}

function total_directories {
        find $1 -type d | wc -l
}

function total_archived_directories {
        tar -tzf $1 | grep  /$ | wc -l
}

function total_archived_files {
        tar -tzf $1 | grep -v /$ | wc -l
}

# creating files
echo "- Creating output files"
touch $output/standard_output.txt
touch $output/error_output.txt

# variable calculations
src_files=$( total_files $input )
src_directories=$( total_directories $input )

# basic echo's
echo ""
echo "- Starting backup of: $input"
echo "  - Bash version: $BASH_VERSION" > $output/standard_output.txt
echo "  - Files to be included: $src_files"
echo "  - Directories to be included: $src_directories" 

# dump output to file 2>
tar -czf $backup_file $input 2> $output/error_output.txt   

# in process calculations
arch_files=$( total_archived_files $backup_file )
arch_directories=$( total_archived_directories $backup_file )

echo "  - Files archived: $arch_files" 
echo "  - Directories archived: $arch_directories" 

echo "  - Backup complete. Located at: $backup_file    ***This will run even if the command fails***"

# using conditionals
if [ $src_files -eq $arch_files ]; then
        echo "  - Backup of $input completed!"
else
        echo "  - **Backup of $input failed!"
fi

