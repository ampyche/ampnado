#!/bin/sh
#to background the process use this commad when invoking
#nohup python3 server.py &>/dev/null &

boo = ps -e | grep "mongod";
echo $boo;
if [ ! $boo ]; then
	sudo mongod --dbpath /var/lib/mongodb --setParameter textSearchEnabled=true;
fi