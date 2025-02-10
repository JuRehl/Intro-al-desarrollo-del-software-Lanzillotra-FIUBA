#i/bin/bash

until (( num > 5 && num <10 ))
do
	#Genera numero random entre 5 y 10
	num=$(( (RANDOM % 10) + 1 ))
	echo "El número generado es: " $num
done
echo "Se termina el loop, salimos con el nro " $num
