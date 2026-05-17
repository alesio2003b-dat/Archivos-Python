#Clases y Objetos 2
#Ejercicio 1
import math
#Ejercicio del Circulo
class Circulo(object):
    #El import math debería estar acá adentro
    def __init__(self,radio):
        self.r=radio
    def Area(self):
        return math.pi * self.r**2
    def Perimetro(self):
        return 2*math.pi*self.r
# a=Circulo(5)
# print(a.Area())
# print(a.Perimetro())
# print(a.Area() + a.Perimetro())

#Ejercicio 2
#Clase Punto
class Punto(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return str((self.x,self.y))
    def distanciaorigen(self):
        distancia=(self.x**2 + self.y**2)**(1/2)
        return distancia
    def mover(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
    def angulo(self):
        return self.x/self.y
    def distanciaotropunto(self,other):
        dis= ((self.x-other.x)**2 + (self.y - other.y)**2)**(1/2)
        return dis
    def __add__(self,other):
        sumax=self.x+other.x
        sumay=self.y+other.y
        return Punto(sumax,sumay)
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __mul__(self,other):
        return (self.x*other.x) + (self.y*other.y)
# a=Punto(4,5)
# b=Punto(6,7)
# print(a.__mul__(b))

#Ejercicio 3
#Clase complejo
class Complejo(object):
    def __init__(self,a,b):
        self.a =a
        self.b =b
    def __str__(self):
        return str(self.a) + "+" + "i" + str(self.b)
    def __add__(self,other):
        a2= self.a + other.a
        b2= self.b + other.b
        return Complejo(a2,b2)
    def __eq__(self,other):
        return self.a==other.a and self.b==other.b

#Ejercicio 4
#Inventario
class Inventario(object):
    def __init__(self):
        self.d={}
    def agregarart(self,id,nombre,cantidad,precio):
        dic={"Nombre":nombre, "Cantidad": cantidad, "Precio": precio}
        self.d.update({id:dic})
    def __str__(self):
        return str(self.d)
    def actualizarart(self,id,nuevacant,nuevop):
        self.d[id].update({"Cantidad":nuevacant, "Precio": nuevop})
    def consultarart(self,id):
        cositas=self.d[447]

        return "Nombre: " +" "+ cositas["Nombre"] + " "+ "Cantidad: " + str(cositas["Cantidad"]) + " " + "Precio: " + str(cositas["Precio"])
    def valortotal(self):
        a=0
        b=0
        valor=0
        for i in self.d:
            for j in self.d[i]:
                beta=self.d[i]
                a=beta["Cantidad"]
                b=beta["Precio"]
            valor=valor+a*b
            a=0
            b=0
        return valor
    def buscarpornonmbre(self,nombre):
        for i in self.d:
            for j in self.d[i]:
                beta=self.d[i]
                if nombre == beta["Nombre"]:
                    c=i
                    break
        return c
    def stocktotal(self):
        a=0
        stock=0
        for i in self.d:
            for j in self.d[i]:
                beta=self.d[i]
                a=beta["Cantidad"]
            stock=stock+a
            a=0
        return stock
    def __str__(self):
        return "Si están leyendo esto, haganlo ustedes :)"
        
    
# a=Inventario()
# a.agregarart(447,"Cepillo de dientes",50,45)
# a.agregarart(524,"Manzana",47,5)
# a.actualizarart(447,42,35)
# print(a.stocktotal())

#Ejercicio 5
#El del libro
class Libro(object):
    def __init__(self,Titulo,Autor,Año,Genero):
        self.t=Titulo
        self.a=Autor
        self.ñ=Año
        self.g=Genero
    def obtenerTitulo(self):
        return str(self.t)
    def obtenerAutor(self):
        return str(self.a)
    #Lo mismo para año y genero
    def establecerTitulo(self,nuevot):
        self.t=nuevot
    def establecernuevoautor(self,nuevoa):
        self.a=nuevoa
    #Lo mismo con los otros dos
    def __str__(self):
       return "Titulo" + ":" + " "+ str(self.t) + "\n" + "Autor" + ":" + " "+ str(self.a) + "\n"+ "Año" + ":" + " "+ str(self.ñ) + "\n" + "Genero" + ":" + " "+ str(self.g) + "\n" 
# a=Libro("Las Aventuras de Alesio","Alesio",2003,"El que más te guste")
# a.establecerTitulo("Alesio :)")
# print(a)

#Ejercicio 6
#El de la moneda
class Moneda(object):
    def __init__(self,nombre,valor,simbolo,codigo,pais):
        self.n=nombre
        self.v=valor
        self.s=simbolo
        self=c=codigo
        self.p=pais
    def actualizarvalor(self,nuevovalor):
        self.v=nuevovalor
    def __eq__(self,other):
        return self.v == other.v
    def convertir(self,other):
        self.v= self.v /other.v *100 #El calculo no es así pero para hacer algo ah
        self.n=other.n
        self.c=other.c
    def __str__(self):
        #Puede estar escrito más lindo lo de abajo con el barra invertida n
        return"Nombre" + " "+ str(self.n) + " "+ "Valor" + " "+ str(self.v)+"Simbolo: " + str(self.s) + "Pais: " + str(self.p)

#Ejercicio 7
#El de los alumnos
class Alumno(object):
    def __init__(self,Nombre,dni,materias={}):
        self.nombre=Nombre
        self.dni=dni
        self.materias=materias
    def info(self):
        return "Nombre: " + str(self.nombre) + "\n"+"DNI" + ":" + " "+ str(self.dni) + "\n"+ str(self.materias)
        # for i in self.materias:
        #     print(str(i) + ":"+ str(self.materias[i]))
    def agregarmateria(self,materianueva):
        self.materias [materianueva]=[]
    def agregarnota(self,materia,notanueva):
        self.materias[materia].append(notanueva)
    def promediogeneral(self):
        a=0
        for i in self.materias:
            a=a+sum(self.materias[i])/len(self.materias[i])
            return a
    def promediomateria(self):
        dic={}
        for i in self.materias:
            a=sum(self.materias[i])/len(self.materias[i])
            dic[i]=a
        return dic
    def aprobado(self,materiarandom):
        a=0
        a=sum(self.materias[materiarandom])/len(self.materias[materiarandom])
        if a>=6:
            return "El alumno está aprobado"
        else:
            "El alumno no está aprobado"

#Ejercicio 8
#Cuentas bancarias
class Cuenta(object):
    def __init__(self,nombreapellido, saldo=0):
        self.n=nombreapellido
        self.s=saldo
    def depositar(self,añado):
        self.s=self.s+añado
    def retirar(self,retiro):
        self.s=self.s+retiro
    def saldoactual(self):
        return str(self.s)
    def recibirdeotracuenta(self,other,recibo):
        self.s=self.s+recibo
        other.s=other.s-recibo
    def transfieroaotracuenta(self,other,doy):
        self.s=self.s-doy
        other.s=other.s+doy
    def __str__(self):
        return str(self.n) + ": " + str(self.s)
    def cuentaaas(self,nombre):
        lista=[]
        with open(nombre,"r") as algo:
            for i in algo:
                a=i.split(";")
                for j in a.strip():
                    lista.append(j)
            return lista
    def guardarcuentas(self,nombre):
        with open(nombre,"w") as algo:
            algo.write(str(self.n) + ";" + str(self.s)+"\n")
# a=Cuenta("Alesio Alesin",500)
# b= Cuenta("Maddi Maddin",600)
# a.transfieroaotracuenta(b,400)
# print(a,b)

####################################################################
#Herencia
#Ejercicio 9 (chat gpt hizo este)
#Figura
# class Figura(object):
#     def area(self):
#         pass
#     def perimetro(self):
#         pass

# class Circulo(Figura):
#     def __init__(self, radio):
#         self.radio = radio
    
#     def area(self):
#         return math.pi * self.radio**2
    
#     def perimetro(self):
#         return 2 * math.pi * self.radio

# class Rectangulo(Figura):
#     def __init__(self, largo, ancho):
#         self.largo = largo
#         self.ancho = ancho
    
#     def area(self):
#         return self.largo * self.ancho
    
#     def perimetro(self):
#         return 2 * (self.largo + self.ancho)

# class Triangulo(Figura):
#     def __init__(self, base, altura, lado1, lado2, lado3):
#         self.base = base
#         self.altura = altura
#         self.lado1 = lado1
#         self.lado2 = lado2
#         self.lado3 = lado3
    
#     def area(self):
#         return 0.5 * self.base * self.altura
    
#     def perimetro(self):
#         return self.lado1 + self.lado2 + self.lado3

# class Cuadrado(Rectangulo):
#     def __init__(self, lado):
# #         #Preguntar cómo hacer
# #         #No pregunté como hacer asi que les toca preguntar a ustedes




# class Alumno(object):
#     def __init__(self,Nombre,dni,materias={}):
#         self.nombre=Nombre
#         self.dni=dni
#         self.materias=materias
#     def __str__(self): #Está no sé si va así o con una función info
#         return "Nombre: " + str(self.nombre) + "\n"+"DNI" + ":" + " "+ str(self.dni) + "\n"+ str(self.materias)
#     def agregarmateria(self,materianueva):
#         self.materias [materianueva]=[]
#     def agregarnota(self,materia,notanueva):
#         self.materias[materia].append(notanueva)
#     def promediogeneral(self):
#         a=0
#         for i in self.materias:
#             a=a+sum(self.materias[i])/len(self.materias[i])
#             return a
#     def promediomateria(self):
#         dic={}
#         for i in self.materias:
#             a=sum(self.materias[i])/len(self.materias[i])
#             dic[i]=a
#         return dic
#     def aprobado(self,materiarandom):
#         a=0
#         a=sum(self.materias[materiarandom])/len(self.materias[materiarandom])
#         if a>=6:
#             return "El alumno está aprobado"
#         else:
#            return "El alumno no está aprobado"

class Alumnouniversitario(Alumno):
    def __init__(self,Nombre,dni,materias,carrera,aprobadas={},regulares={}):
        super().__init__(Nombre,dni,materias)
        self.c=carrera
        self.aprobadas=aprobadas
        self.reg=regulares
    def regularizar(self,materia):
        a={}
        for i in self.materias:
            if i!=materia:
                a[i]=self.materias[i]
        self.reg[materia]=self.materias[materia] #Acá lo que hago es que La materia en regulares tenga la nota que está en materias 
        self.materias=a #Acá hago que self.materias no tenga a materia
    def aprobada(self,materia,regular=True):
        if regular==True:
            b={}
            for i in self.reg:
                if i!=materia:
                    b[i]=self.reg[i]
            self.aprobadas[materia]=self.reg[materia]
            self.reg=b
        elif regular==False:
            c={}
            for i in self.materias:
                if i!=materia:
                    c[i]=self.materias[i]
            self.materias=c
    def promeiogen(self):
        prom=[]
        for i in self.aprobadas:
            prom.append(self.aprobadas[i])
        return sum(prom)/len(prom)
a=Alumno("Alumno1",442,{"Fisica":[9,8,9],"Química":[8,7,8],"Futbol":[10,10,10],"Amor":[1,2,3]})
# a.agregarmateria("Noseque")
# a.agregarnota("Noseque",7)
# a.agregarnota("Noseque",8)
# a.agregarnota("Noseque",9)
# print(a)
# b=Alumnouniversitario("Alumno2",442,{"Fisica":[9,8,9],"Química":[8,7,8],"Futbol":[10,10,10],"Amor":[1,2,3]},"Fiisica")   
# b.agregarmateria("Fuchibol")
# b.agregarnota("Fuchibol",8)
# b.agregarnota("Fuchibol",9)
# b.regularizar("Fuchibol")
# b.regularizar("Fisica")
# b.regularizar("Química")
# b.aprobada("Fuchibol")
# b.aprobada("Química")
# b.aprobada("Amor",False)
# print(b)



#Ejercicio 12
#Billetera virtual
class BilleteraVirtual(Cuenta):
    def __init__(self, nombreapellido, saldo=0, servicios={},numerodetarjeta=0):
        super().__init__(nombreapellido, saldo)
        self.serv=servicios
        self.num=numerodetarjeta
        self.pagados={}
        self.pendien=self.serv
    def agregarservicio(self,servicio,fechadevenc):
        self.serv[servicio]=fechadevenc
    def pagarservicio(self,servicio,montodepago):
        self.s=self.s-montodepago
        self.pagados[servicio]=self.serv[servicio]
        self.pendien.pop(servicio)
    def pendientes(self):
        return str(self.pendien)
    def numerodetarjeta(self):
        return str(self.num)
# b=BilleteraVirtual("Alesio Alesin",500,{"Luz": "9/12/18","Agua": "18/12/9", "Gas" : "1/2/2024"},4546546)
# b.pagarservicio("Luz",490)
# print(b.numerodetarjeta())


    
