#!/bin/bash

cd /sys/class/gpio/

# GPIO exportieren

echo "20" > export
echo "26" > export

# GPIO auf Output setzen

echo "out" > gpio20/direction
echo "out" > gpio26/direction

# GPIO Werte auf 1 Setzen

echo "1" > gpio20/value
echo "1" > gpio26/value