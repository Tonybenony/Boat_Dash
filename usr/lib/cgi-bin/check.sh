#!/bin/bash
echo -e "Content-type: text/html\n\n"
 
echo "<h1>Raspberry Pi GPIO </h1>"
 
echo  $(date)
echo  "<pre>"
gpio readall 
echo "</pre>"

OUTPUT1=$(gpio -g read 23)
OUTPUT2=$(gpio -g read 24)
OUTPUT3=$(gpio -g read 17)
OUTPUT4=$(gpio -g read 27)
OUTPUT5=$(gpio -g read 22)
OUTPUT6=$(gpio -g read 5)

echo"<body onload='Check(23)'>"
echo"<body onload='Check(24)'>"
echo"<body onload='Check(17)'>"
echo"<body onload='Check(27)'>"
echo"<body onload='Check(22)'>"
echo"<body onload='Check(5)'>"