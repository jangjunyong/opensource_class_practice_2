#!/bin/bash

func(){
   ls
   if ! test -d $1 ;then
      mkdir $1
   fi
   cd $1
   for i in 0 1 2 3 4
   do
      touch file$i.txt
      echo "file$i.txt created"
   done
   tar -cvf $1.tar *
   mkdir $1
   mv $1.tar $1
   cd $1
   tar -xvf $1.tar
}

echo "프로그램을 시작하겠습니다."
func $1

echo "프로그램을 종료하겠습니다."
	
