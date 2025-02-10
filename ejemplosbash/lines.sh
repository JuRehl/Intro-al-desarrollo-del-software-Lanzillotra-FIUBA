#!/bin/bash

touch lines.txt

for i in {1..100}; do
	echo "$i" >> lines.txt
done
