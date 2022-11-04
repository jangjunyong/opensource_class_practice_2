#!/bin/sh

showinfo(){
	ls $1
}

echo "프로그램을 시작합니다."

echo "함수안으로 들어왔음"

read input

showinfo $input

echo "프로그램을 종료합니다."

exit 0
