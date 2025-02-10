#!/bin/bash

for i in {1..10}; do
	echo "Ingresa un número: "
	read n
	let SUMA+=$n
done
PROMEDIO= $(($SUMA/10))
echo "El promedio de los 10 números es: " $PROMEDIO

