#!/bin/sh

bmi=$(echo "scale=1;10000.0*$1/$2/$2" | bc)
if [ $(echo "$bmi > 23" | bc) -eq 1 ]
then
	echo "과체중"
elif [ $(echo "$bmi > 18.5" | bc) -eq 1 ]
then
	echo "정상"
else
	echo "저체중"
fi
exit 0
