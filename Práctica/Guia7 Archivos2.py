#Archivos2
#Ejercicio 1
#Escribir renglones
# def escribirrenglones(nombre,renglones):
#     with open(nombre,"w") as algo:
#         for i in renglones:
#             algo.write(str(i)+ "\n")
# nombre="Renglón"
# renglones=["Hola","Mundo","Soy","Hola"]
# print(escribirrenglones(nombre,renglones))

#Imprimir lo que dice el archivo
# def leerarchivo(nombre):
#     with open(nombre,"r") as algo:
#         for i in algo:
#             print(i[:-1]) #Si lo escribo así, quita la separación grande entre los renglones
# print(leerarchivo("Renglón"))

#Contar lineas
# def contarlineas(nombre):
#     a=0
#     with open(nombre,"r") as algo:
#         for i in algo:
#             a=a+1
#     return a
# print(contarlineas("Renglón"))

#Primeras n lineas
# def nlinea(nombre,n):
#     a=1
#     with open(nombre, "r") as algo:
#         for i in algo:
#             if a<=n:
#                 print(i[:-1]) #Ese -1 es para que no imprima el salto de pagina (el barra n)
#             a=a+1
# print(nlinea("Renglón",2))

#Adjuntar Renglones
# def adjuntar(nombre,renglones):
#     with open(nombre,"a") as algo:
#         for i in renglones:
#             algo.write(str(i)+"\n")
# renglones=["Hola","Mundo","Soy","Hola"]
# adjuntar("Renglón",renglones)

#Hacer archivo lista
# def listarchivo(nombre):
#     lista=[]
#     with open(nombre, "r") as algo:
#         for i in algo:
#             lista.append(i.strip()) #El strip quita el\n 
#     return lista
# print(listarchivo("Renglón"))

# Copiar archivo
# def copiararchivo(lectura,escritura):
#     lectura=open(lectura,"r")
#     with open(escritura,"w") as algo:
#         for i in lectura:
#             algo.write(str(i))
# print(copiararchivo("Renglón", "Bicicleta"))

#Contar Caracter
# def contar(nombre,caracter):
#     a=0
#     with open(nombre,"r") as algo:
#         for i in algo:
#             b=i.strip().split()
#             for j in b:
#                 for k in j:
#                     if k==caracter:
#                         a=a+1
#     return a
# #Tiene un costo computacional alto, si se quiere optimizar, hay que
# #sacar el ultimo for, hacer qe b no exista y dejar el for j in i.strip(), y meter ahí el if
# print(contar("Renglón", "o"))

#Ejercicio 2
#Escribir Tabla de Multiplicar:
# def tablas(nombre,n):
#     with open(nombre,"w") as algo:
#         for i in range(1,11):
#             algo.write(f"{n} x {i} = {n*i}" + "\n")
# print(tablas("Tablas", 5))

#Ejercicio 3
#Tabla con prefijo
# def creartabla(prefijo):
#     for i in range(1,11):
#         with open(f"{prefijo}_{i}","w") as algo:
#             for j in range(1,11):
#                 algo.write(f"{i} x {j} = {i*j}" + "\n")
# print(creartabla("Tablas"))

#Ejercicio 4
#Estadísticas del Mundial
# def mundial(nombre):
#     #Lo genero yo al archivo porque no sé como descargarlo
#     archivo = open(nombre, 'w')
#     archivo.write('1 - 2\n')
#     archivo.write('2 - 0 \n')
#     archivo.write('2 - 1\n')
#     archivo.write('2 - 1\n')
#     archivo.write('2 - 2\n')
#     archivo.write('3 - 0\n')
#     archivo.write('3 - 3\n')
#     archivo.close()
#     with open(nombre,"r") as algo:
#         ganados=0
#         perdidos=0
#         empates=0
#         golesfav=0
#         golesenc=0
#         for i in algo:
#             a=i.strip().split() #Podría haber puesto el "-" en el split pero bueno
#             if a[0]>a[-1]:
#                 ganados=ganados+1
#             elif a[0]<a[-1]:
#                 perdidos=perdidos+1
#             else:
#                 empates=empates+1
#             golesfav=golesfav+ int(a[0])
#             golesenc=golesenc+ int(a[-1])
#         print("Los partidos ganados son: ",ganados,". Los perdidos son: ",perdidos, ". Mientras que los empatados son: ",empates,". Se metieron en total: ",golesfav, "goles, y se recibieron un total de: ",golesenc,".")
# print(mundial("mundial"))
##############################################################################################################################################################################################################################
#Archivos csv

#Ejercicio 5
#Instrucciones
# archivo = open('animales.csv', 'w')
# archivo.write('Nombre;Especie;Edad\n')
# archivo.write('Canela;Perro;5\n')
# archivo.write('Pelusa;Gato;3\n')
# archivo.write('Aurelio;Tortuga;14\n')
# archivo.close()

#Ejercicio 6
#Leer animales
# def leeranimales(nombre):
#     claves=["Nombre","Especie","Edad"]
#     lista=[]
#     dic={}
#     with open(nombre,"r") as algo: 
#         for i in algo:
#             a=i.strip().split(";")
#             for j in range(len(a)):
#                 dic[claves[j]]=a[j]
#             lista.append(dic)
#             dic={}
#     lista.remove(lista[0]) #Esto es para sacar la lista que se hace con los titulos "Nombre, Especie y Edad"
#     return lista
# print(leeranimales("animales.csv"))

#Ejercicio 7
#Tablas notas
# def tablasnotas(nombre,alumnos,parcial1,parcial2):
#     promedio=["Promedio"]
#     for i in range(1,4):
#         a=(Parcial1[i] + Parcial2[i])/2
#         promedio.append(a)
#     with open(nombre,"w") as algo:
#         for i in range(len(Alumnos)):
#             algo.write(str(Alumnos[i])+";"+str(Parcial1[i])+";"+ str(Parcial2[i])+";"+str(promedio[i]) + "\n")
# Alumnos=["Nombre","Juan", "María", "Carlos"]
# Parcial1=["Parcial 1",85, 92, 78] 
# Parcial2=["Parcial 2",90, 88, 81]
# print(tablasnotas("Archivonotas.csv",Alumnos,Parcial1,Parcial2))

#Ejercicio 8
#Funcion 
# def funcion(nombre,f,ini,fin):
#     j=[i for i in range(ini,fin+1)]
#     y=[f(j) for j in j]
#     with open(nombre, "w") as algo:
#         algo.write("X"+";"+"f(x)"+"\n")
#         for i in range(len(j)):
#             algo.write(str(j[i])+";"+str(y[i])+"\n")
# print(funcion("funcion.csv",lambda x: x*x,0,10))

