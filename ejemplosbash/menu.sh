#!/bin/bash

echo "Ingrese un archivo "
read ar

echo "1 Ingresa una palabra y se reemplaza por *** "
echo "2 Abre el archivo"
echo "3 Realiza una copia del archivo llamada meni_copia.sh"
echo "4 Ingresa un email y se valida mediante RE"
echo "5 Salir"

read a
case $a in
1)  echo "Cambiar palabra por *** del archivo $ar"
    echo "Ingresa la palabra a cambiar: "
    read palabra
    sed s/$palabra/***/g $ar
    ;;
2)  echo "Abre el archivo"
    nano $ar
    ;;
3)  echo "Realizando copia del archivo"
    cp $ar menu_copia.sh
    ;;
4)  echo "Ingresa un email y se valida"
    echo "Ingrese un mail: "
    read e
    [A-Za-z]{2,}\@[a-z]{2,}\.[a-z]{2,} $ar
    ;;
5)  echo "Salir"
esac

