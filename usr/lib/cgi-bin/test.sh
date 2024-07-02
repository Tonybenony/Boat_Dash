#!/bin/bash
echo -e "Content-type: text/html\n\n"
 
echo "<h1>Raspberry Pi GPIO </h1>"
 
echo  $(date)
echo  "<pre>"
gpio readall 
echo "</pre>"

gpio -g mode $1 out

OUTPUT=$(gpio -g read $1)

if [ $OUTPUT == 1 ]
then

gpio -g write $1 0
else

gpio -g write $1 1

fi