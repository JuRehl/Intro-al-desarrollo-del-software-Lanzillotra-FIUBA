#!/bin/bash


if [ -z $(ls -A) ]
then
	echo "Como quieres llamar a tu entorno virtual?"
	read entorno
        if [ -z "$entorno" ]
        then
                echo "El nombre del entorno no puede estar vacio"
                exit
        fi

	virtualenv "$entorno"

else
	echo "El directorio debe estar vacio"
	exit
fi

touch app.py

cat <<EOF >> app.py
from flask import Flask, render_template,url_for,request,abort

app = Flask(__name__)

@app.route('/')
def algo():
	return render_template("base.html")


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
EOF


mkdir templates
cd templates
touch base.html

cat <<EOF >> base.html
<!DOCTYPE html>
<html>
	<head>
		<title>  </title>
	</head>

	<body>
	</body>

</html>

EOF


cd ..


mkdir static
cd static
mkdir js
mkdir css
mkdir img

cd ..

echo 'Estructura flask creada con exito'

