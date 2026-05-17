def cveinstein(T):
    import numpy as np
    import matplotlib.pyplot as plt
    k_B = 1.380649e-23  # Constante de Boltzmann en J/K
    N = 1.139e23  # Número de átomos (por ejemplo, para 12.025 g de cobre)
    x=580/T
    cv=3 *1.559* (x**2) * (np.exp(x) / (np.exp(x) - 1)**2)
    return cv
def hallarT(nombre):
    import numpy as np
    import matplotlib.pyplot as plt
    dm=[]
    Tobt=[]
    Tes=[]
    cvsf=[]
    cvsr=[]
    Tc=[]
    error=[]
    L=197.7
    n=0.189
    with open(nombre,"r") as algo:
        for i in algo:
            a=i.strip().split()
            dm.append(float(a[1]))
            Tes.append(float(a[0]))
    for i in range(len(dm)):
        b=cveinstein(Tes[i])
        cvsr.append(b)
        Tob=((L*dm[i])/(n*b))+77
        Tobt.append(Tob)
        Tc.append(Tob-273.15)
        #dmo=b*n*(Tes[i]-77)/L
        #Tc.append(dmo)
    for i in range(len(dm)):
        o=(L*dm[i])/(n*(Tes[i]-77))
        m=(L*0.02)/(n*Tes[i]-77)
        cvsf.append(o)
        error.append(m)
    #plt.plot(Tobt,cvsf,"o",color="blue")
    plt.plot(Tes,cvsf,"o",color="red")
    plt.plot(Tes,cvsr,"o",color="green")
    print(Tc)
    with open("cvrar.txt","w") as algo:
        for i in range(len(dm)):
            algo.write(f"{Tes[i]} {cvsf[i]} {error[i]} {Tes[i]-273.15}\n")
    return plt.show()
print(hallarT("cobreya.txt"))