#!/bin/bash

# awk
#   - materials: https://docstore.mik.ua/orelly/unix/sedawk/examples/index.htm

#
# invoking awk: awk 'instructions' files
#   - [options]: [-F -f]
#   - executes a set of instructions for each line of input
#       - $0 represents the entire input line. $1, $2,...,$n refer to the individual fields on the input line
#   - awk program can be used more like a query language

# Error modes
#   - Not enclosing a procedure within braces ({}) 
#   - Not surrounding the instructions within single quotes (`') 
#   - Not enclosing regular expressions within slashes (//)

# Using scripts
echo ""
echo "- printing fields"
awk -f scripts/awkscr_printfields data/list

echo ""
echo "- specifying delimeters"
awk -F, -f scripts/awkscr_printfields data/list

echo ""
echo "- applying scripts to line patterns"
awk -F, -f scripts/awkscr_patterns data/list


