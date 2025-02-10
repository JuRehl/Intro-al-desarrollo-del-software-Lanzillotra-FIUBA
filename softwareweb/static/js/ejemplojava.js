let numero1 = "123"

console.log(numero1)

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

//Iterar por elementos no indices

let alumnos=["Pala","Martin","Bruno"]
for (const alumno of alumnos) {
    console.log(alumno)
}
//buscar en que casos se usa of y en que casos se usa in

const alumno= {
    nombre:"Pala",
    edad:23,
    prop:2
}
for (prop in alumno) {
    console.log(prop + ": " + alumno[prop])
}

const nums=[57,58,6]
console.log(nums[3])

function modulo(x, y) {
    const sumaCuadrados = x*x + y*y
    const resultado = Math.sqrt(sumaCuadrados)
    return resultado
}

//Llamo e imprimo la funcion
console.log(modulo(3,4))

const modulo1 = function(x, y) {
    return Math.sqrt(x*x + y*y)
}

// Función flecha o "arrow function"
// (args) => returnValue
const suma = (x, y) => x + y
console.log(typeof suma)  // function
console.log(typeof modulo1)  // function
console.log(suma(2, 3))  // 5
console.log(modulo1(4,6)) //7.21

console.log(((x,y)=> Math.sqrt(x*x + y*y))(2,3))
