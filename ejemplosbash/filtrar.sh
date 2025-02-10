#!/bin/bash

lista = ls -d D*
for i in [$lista];do
	contienen=grep "top" in $lista
	touch salida.txt
	echo $contienen >> salida.txt
done
