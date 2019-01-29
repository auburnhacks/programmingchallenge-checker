#!/bin/sh

#Enter your name here
YOURNAME="name1"

echo $YOURNAME
start="$(date +%s.%N)"

#Compile/run your code here
python3 prob.py


end="$(date +%s.%N)"
time_elapsed="$(echo $end-$start | bc)"
echo $time_elapsed
