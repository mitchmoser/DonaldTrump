#!/bin/bash
# check to see if trump.py is running
var=$(pgrep -f trump.py)
# if it is not, start it in the background
if [[ ! "$var" ]]
then
	python3 /path/to/file/trump.py &
fi
exit 0
