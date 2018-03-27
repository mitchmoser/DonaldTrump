#!/bin/bash
# check to see if script is running
var=$(pgrep -f trump.py)
# if it is not, start it
if [[ ! "$var" ]]
then
	python3 /path/to/file/trump.py
fi
exit 0
