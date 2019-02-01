#!/bin/sh

# Enter your name here
YOURNAME="YOUR_NAME_HERE"

echo $YOURNAME
start="$(date +%s.%N)"

# Compile/run your code here



end="$(date +%s.%N)"
time_elapsed="$(echo $end-$start | bc)"
echo $time_elapsed
