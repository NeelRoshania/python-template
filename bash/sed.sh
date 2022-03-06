#!/bin/bash

# sed
#   - materials: https://docstore.mik.ua/orelly/unix/sedawk/examples/index.htm

#
# invoking sed: sed command [options] script file
#   - executes a set of instructions for each line of input
#   - sed -f script files
#

# Error modes
#   - 

# 3 ways to specify multiple arguments
echo ""
echo "- one argument"
sed 's/ MA/, Masschussets/; s/ PA/, Pennsylvania/' data/list

echo ""
echo "- suppressing output"
sed -n -e 's/ MA/, Massachussets/' -e 's/ PA/, Pennsylvania/' -e 's/ CA/, California/' data/list

echo ""
echo "- multiple arguments"
sed '
s/ MA/, Masschussets/
s/ PA/, Pennsylvania/
s/ CA/, California/' data/list

# specifying script file and saving to output
#   >> appending
#   > create and/or overwrite existing file

echo ""
echo '- specifying script file'
sed -f scripts/sedscr data/list > data/sedscr_output

# xargs