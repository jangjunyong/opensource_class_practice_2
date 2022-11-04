#!/bin/sh

echo "리눅스가 재밌나요? (yes / no)"
read answer
case $answer in
	yes|y|Y|YES|Yes)
		echo "yes";;
	No|n|N|no)
		echo "no";;
	*)
		echo "yes or no로 입력";;
esac
exit 0
	
















