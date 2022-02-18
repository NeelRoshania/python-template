#!/bin/bash

# Sed & Awk
#   - materials: https://docstore.mik.ua/orelly/unix/sedawk/examples/index.htm

#
# Using sed & awk
#   - pipe sed into awk
#       - use sed to find patterns 
#       - used awk to apply logic to output of sed


# Error modes
#   - 

# Using scripts
echo ""
echo "- piping (|) sed into awk (no need to specify file in awk"
sed -f scripts/sedscr data/list | awk -F, -f scripts/awkscr_printfields

echo ""
echo "- applying sort"
sed -f scripts/sedscr data/list | awk -F, -f scripts/awkscr_printfields | sort

