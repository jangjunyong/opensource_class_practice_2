#!/bin/sh

read dir
if [ ! -d $dir ];then
	mkdir $dir
fi
	
cd $dir
for i in 0 1 2 3 4 
do
	newdir="$dir$i"
	mkdir $newdir
	fname="$dir$i.txt"
	touch $fname
done

for i in 0 1 2 3 4
do
	location="$dir$i.txt"
	todir="$dir$i/$location"
	ln -Tfs $location $todir
	done





