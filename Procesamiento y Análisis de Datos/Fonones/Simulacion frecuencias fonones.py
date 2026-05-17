def cuerdadesnuda():
    import math
    import matplotlib.pyplot as plt
    T=59.782
    mu=0.000703
    L= 2.48
    w=[]
    x=[]
    for i in range(1,40):
        a=math.sqrt(T/mu)*i*math.pi/(L*2*math.pi)
        w.append(a)
        x.append(i)
        print(w)
    plt.plot(x,w)
    return plt.show()
print(cuerdadesnuda())

def cuerdamonoatomica():

    import math
    import matplotlib.pyplot as plt
    T=59.782
    m=0.001915
    w=[]
    x=[]
    L=2.486
    a=L/11
    for i in range(1,11):
        g=math.sqrt(4*T/(m*a))*math.fabs(math.sin(i*math.pi/(22)))
        w.append(g/(2*3.14)) 
        x.append(i)
    print(w)
    plt.plot(x,w, "o")
    plt.plot(x,w,label="Modos teóricos")
    plt.plot((1,2,3,4,5,6,7,8,9,10),(22.316,36.151,46.790,62.58,75.05,83.80,99.96,107.3,112.251,117.505),"*")
    plt.legend()
    return plt.show()
print(cuerdamonoatomica())


def cuerdadiatomica():
    import math
    import matplotlib.pyplot as plt
    T=59
    m2=0.0019127
    m3=0.00078
    w1=[]
    w2=[]
    x=[]
    L=2.48
    a=L/11
    for i in range(1,6):
        g=2*T/a *(1/m2 + 1/m3)*(1 + math.sqrt(1-(4*m2*m3)/((m3+m2)**2)*math.sin(i*math.pi/(11))**2))
        h=2*T/a *(1/m2 + 1/m3)*(1 - math.sqrt(1-(4*m2*m3)/((m3+m2)**2)*math.sin(i*math.pi/(11))**2))
        w1.append(math.sqrt(g)/6.14)
        w2.append(math.sqrt(h)/6.14)
        x.append(i)
    print(w1)
    print(w2)
    plt.plot(x, w1)
    plt.plot(x,w1,"o", label= "Modos ópticos teóricos")  # Graficar la función seno
    plt.plot((5,4,3,2,1),(188.357,199.4,205.75,215.50,223.25),"*",label="Modos ópticos Medidos")
    plt.plot(x, w2)
    plt.plot(x,w2,"o",label= "Modos Acústicos teóricos")
    plt.plot((1,2,3,4,5),(26.49,59.190,75.02,99.95,117.79), "*",label= "Modos ópticos Medidos")
    plt.legend()
    return plt.show()
print(cuerdadiatomica())



