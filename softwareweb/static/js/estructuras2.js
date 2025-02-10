let numero = 8

if (numero < 20) {
    console.log("El número es menor a 20")
} else if (numero == 20) {
    console.log("El número es igual a 20")
} else {
    console.log("El número es mayor a 20")
}

while (numero < 20) {
    numero++  // numero = numero + 1
}

for (let i=1; i<5; i++) {
    const nuevoValor = numero + i
    console.log("Ahora el número vale: " + nuevoValor)
}
