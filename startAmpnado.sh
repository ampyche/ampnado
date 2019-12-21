#!/bin/sh
#to background the process use this commad when invoking
#nohup python3 server.py &>/dev/null &

boo = "/usr/share/ampnado/server.py"
if [ -f $boo ]; then
	python3 $boo
fi