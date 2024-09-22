#!/bin/bash

wget https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz
tar -xzf lab3-bundle.tar.gz

# tr can remove spaces
cat lab3_data.tsv | tr -s '\n' > my_new_file.tsv

# Use `tr` - "translate"
tr '\t' ',' < my_new_file.tsv > myfile.csv

REMAINING_LINES=$(tail -n +2 myfile.csv | wc -l)
echo $REMAINING_LINES

tar -czvf converted-archive.tar.gz myfile.csv
