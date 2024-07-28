#!/bin/bash

gpio -g write 23 1
gpio -g write 24 1
gpio -g write 27 1
gpio -g write 27 1
gpio -g write 22 1
gpio -g write 5 1
gpio -g write 6 1
gpio -g write 26 1
gpio -g write 16 0

gpio -g mode 23 out
gpio -g mode 24 out
gpio -g mode 27 out
gpio -g mode 27 out
gpio -g mode 22 out
gpio -g mode 5 out
gpio -g mode 6 out
gpio -g mode 16 out

# Beeper

gpio -g write 16 1
sleep 0.1
gpio -g write 16 0
sleep 0.1
gpio -g write 16 1
sleep 0.1
gpio -g write 16 0
