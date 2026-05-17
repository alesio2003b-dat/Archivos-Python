def masas(nombre):
    nueva=[]
    a=0
    with open(nombre,"r") as algo:
        for i in algo:
            if a>0:
                b=i.strip().split()
                nueva.append(b[0])
            a=a+1
    return nueva

def nuevo(archivo,nombrenuevo,material,efervece,tmax):
    import matplotlib.pyplot as plt
    masa=masas(archivo)
    t=[]
    masaplot=[]
    tplot=[]
    
    u=0
    for i in range(len(masa)):
        u=u+0.0525
        t.append(u)
    print(t)
    for i in range(len(t)):
        if t[i]>=efervece:
            h=i
            break
    cobre=12.025
    aluminio=5.28
    niquel=2.41
    silicio=1.72
    if material=="cobre":
        elemento=cobre
    elif material=="aluminio":
        elemento=aluminio
    elif material=="niquel":
        elemento=niquel
    elif material=="silicio":
        elemento=silicio   
    masausable=[]
    for i in range(len(masa)):
        if float(masa[i+1])>float(masa[i]) and t[i]>15:
            c=i-1
            break
    for i in range(len(masa)):
        if i<c:
            masausable.append(masa[i])
        if i>=c:
            masaa=float(masa[i])-elemento
            masausable.append(masaa)    
    with open(nombrenuevo,"w") as beta:
        for i in range(len(masa)):
            if i<c:
                masaplot.append(float(masa[i]))
                tplot.append(t[i])
                beta.write(f"{ str(t[i])} {masa[i]} {'-'}\n")
            if i>=h and t[i]<tmax:
                masaplot.append(float(masa[i])-elemento)
                tplot.append(t[i])
                beta.write(f"{str(t[i])} {'-'} {float(masa[i])-elemento}\n")
    plt.plot(tplot,masaplot,"o",markersize=1)
    return plt.show()
print(nuevo("cobreambiente.txt.txt","cobresi.txt","cobre",63,150))
