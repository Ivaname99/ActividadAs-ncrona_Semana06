#Saludo dependiendo de la hora
import datetime
fechaActual = datetime.datetime.now()
horaTexto = "19:00:00"
horaTexto2 = "12:00:00"

horaActual = datetime.datetime.strftime(fechaActual, "%H:%M:%S")
horaT = datetime.datetime.strptime(horaTexto,"19:00:00")
horaT2 = datetime.datetime.strptime(horaTexto2,"12:00:00")

if (horaActual >= horaTexto):
    saludo = "Buenas noches"
else:
    if (horaActual >= horaTexto2):
        saludo = "Buenas tardes"
    else:
        saludo = "Buenos días"
        
#Saludo
print(saludo,"""Ingeniero Carballo
En este sistema estaremos realizando los problemas matematicos planteados
en la guía utilizando los operadores aritméticos que se nos indicó.""")
print()
print("Indicaciones planteadas")
print()
print("Elija tres variables")
print(6)
print(7)
print(3)
print()

#Variables
var1 = 6
var2 = 7
var3 = 3
sumaResultado = var1 + var2 + var3
productoResultado = var1 * var3
exponenteResultado = productoResultado ** var2
moduloResultado = var1 % var2
salida = "El resultado es:"

#Suma de variables
print(f"Sume las variables: {var1} + {var2} + {var3}.")
print(salida,sumaResultado)
print()

#Reste las variables siendo la tercera variable mas alta que la primera.
print(f"Reste las variables: {var2} - {var1} - {sumaResultado} - {var3}")
print(salida,var2 - var1 - sumaResultado - var3)
print()

#Multiplicar 2 variables asignarlas a otra variable y esa variable multiplicarla por la segunda variable de la suma y la resta.
print(f"Multiplique las variables: {productoResultado} * {var2} * {var1}")
print(salida,productoResultado * var2 * var1)
print()

#Sacar a la primera variable de la multiplicación el exponente de la segunda variable de la multiplicación.
print(f"Resuelva el siguiente exponente: {productoResultado}^{var2}")#Nota: usamos ^ pero solo en el texto, en el desarrollo pusimos **.
print(salida,productoResultado ** var2)
print()

#Sacar el módulo de la primera variable de la suma con la primera variable de la resta.
print(f"Saque el módulo de: {var1} % {var2}")
print(salida,var1 % var2)
print()

#Dividir la variable resultado del exponente entre la variable resultado del módulo.
print(f"Realize la división de: {exponenteResultado} / {moduloResultado}")
print(salida,exponenteResultado / moduloResultado)
print()

#Realizar la división entera de la división normal.
print(f"Realize la división entera de: {exponenteResultado} // {moduloResultado}")
print(salida,exponenteResultado // moduloResultado)
print()
