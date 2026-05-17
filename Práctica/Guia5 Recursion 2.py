#Recursion 2
#Ejercicio 1
#Suma de Gauss
# def sumagauss(n):
#     if n==1:
#         r=1
#     else:
#         r=n+sumagauss(n-1)
#     return r
# print(sumagauss(5))

#Ejercicio 2
#Cantidad de digitos
# def contardigitos(n):
#     if abs(n)<10:
#         r=1
#     else:
#         r=1+contardigitos(n/10)
#     return r
# print(contardigitos(-100))

#Ejercicio 3
#Cociente
# def cociente(a,b):
#     if a>= b:
#         r=1 + cociente(a-b,b)
#     else:
#         r=0
#     return r
# print(cociente(5,5))

#Ejercicio 4
#Sumar lista
# def sumarlista(l):
#     if len(l)==0:
#         r=0
#     else:
#         r=l[-1]+sumarlista(l[0:len(l)-1])
#         return r

#Ejercicio 5
#Sumar digitos:
# def sumardigitos(n):
#     n=str(n)
#     if len(n)==0:
#         r=0
#     else:
#         r= int(n[-1]) + (sumardigitos((n[0:len(n)-1])))
#     return r
# print(sumardigitos(452))

#Ejercicio 6
#Armonía elemntal 
# def armonia(n):
#     if n==0:
#         r=0
#     else:
#         r=1/n + armonia(n-1)
#     return r
# print(armonia(4))

#Ejercicio 7
#Potencia
# def potencia(a,b):
#     if b==0:
#         r=0
#     if b==1:
#         r=a
#     else:
#         r=a*potencia(a,b-1)
#     return r
# print(potencia(3,4))

#Ejercicio 8
#Buscar elemento
# def buscarelemento(lista,elemento):
#     if len(lista)==0:
#         return False
#     if lista[-1]==elemento:
#         return True
#     else: 
#        return buscarelemento(lista[0:len(lista)-1],elemento)
# lista=[1,3,4,5,6]
# elemento=3
# print(buscarelemento(lista,elemento))

#Ejercicio 9
#Hojas
# def hojaA(n):
#     if n==0:
#         ancho=841
#         largo=1189
#     else:
#         anchoo=hojaA(n-1)[0]
#         largoo=hojaA(n-1)[1]
#         ancho= largoo//2 
#         largo=anchoo
#     return (ancho,largo)
# print(hojaA(4))

#Ejercicio 10
#Par Impar
# def Par(n):
#     if n==0:
#         r=True
#     else:
#         r=impar(n-1)
#     return r

# def impar(n):
#     if n==0:
#         r=False
#     else:
#         r=Par(n-1)
#     return r

# print(Par(18)) 


