#Problema 1

# Lista original
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

# Quitar repetidos
lista_sin_repetidos = []
for numero in lista_original:
    if numero not in lista_sin_repetidos:
        lista_sin_repetidos.append(numero)

# Mostrar resultado
print("Lista sin repetidos:", lista_sin_repetidos)

#Problema 2

archivo = input("Nombre del archivo: ").strip().lower()

if archivo.endswith(".gif"):
    print("image/gif")
elif archivo.endswith(".jpg") or archivo.endswith(".jpeg"):
    print("image/jpeg")
elif archivo.endswith(".png"):
    print("image/png")
elif archivo.endswith(".pdf"):
    print("application/pdf")
elif archivo.endswith(".txt"):
    print("text/plain")
elif archivo.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

#Problema 3:

for n in range(1500, 2701):
    if n % 7 == 0 and n % 5 == 0:
        print(n)

#Problema 4:

 # Patrón de asteriscos

for fila in range(1, 6):
    print("* " * fila)

for fila in range(4, 0, -1):
    print("* " * fila)

#Problema 5:
numeros = [] ; pares = 0 ; impares = 0

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ")
    if respuesta == "NO":
        break
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
        if numero % 2 == 0: pares += 1
        else: impares += 1

print("Números ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

#Problema 6:

alumnos=[]
n=int(input("Cuantos alumnos?: "))

for i in range(n):
    nombre=input("Nombre: ")
    notas=[]
    for j in range(3):
        nota=int(input("Nota: "))
        notas.append(nota)
    alumno={"Alumno":nombre,"Notas":notas}
    alumnos.append(alumno)

print(alumnos)

#Problema 7:

suma=0
for n in range(2,100):
    primo=True
    for i in range(2,n):
        if n%i==0:
            primo=False
            break
    if primo:
        suma+=n
print("Suma:",suma)

#Problema 8:

a,b=0,1
while a<=50:
    print(a)
    a,b=b,a+b

#Problema 9:

n = 1
while n < 1000:
    suma = 0
    div = 1
    while div < n:
        if n % div == 0:
            suma = suma + div
        div = div + 1
    if suma == n:
        print("Número perfecto:", n)
    n = n + 1

#Problema 10:

def factorial(n):
    if n < 0:
        return "El número debe ser no negativo"
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

#Problema 11:

def sin_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = ""
    for caracter in texto:
        if caracter in vocales:  
            resultado += caracter
    return resultado

frase = input("Ingrese un texto: ")
print(sin_vocales(frase))

#Problema 12: 

def convertir_fecha(fecha):
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
             "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

    if "/" in fecha:
        partes = fecha.split("/")
        mes = int(partes[1])
        dia = int(partes[0])
        año = int(partes[2])
    else:
        partes = fecha.split()
        mes = meses.index(partes[0])
        dia = int(partes[1].replace(",", ""))
        año = int(partes[2])

    return f"{año}-{mes:2}-{dia:2}"

entrada = input("Ingrese una fecha: ")
print(convertir_fecha(entrada))


















