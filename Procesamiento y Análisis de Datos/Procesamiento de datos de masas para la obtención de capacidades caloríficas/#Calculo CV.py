#Calculo CV
def cvt(nombre,moles):
    import matplotlib.pyplot as plt
    L=199.1
    Temp=[]
    dm=[]
    cv=[]
    with open(nombre,"r") as algo:
        for i in algo:
            a=i.strip().split()
            print(a)
            Temp.append(float(a[0])+float(273.15))
            dm.append(float(a[1]))
    for i in range(len(Temp)):
        v=(L*dm[i])/(moles*(Temp[i]-77))
        cv.append(v)
    plt.plot(Temp,cv,"o")
    with open("cvcobre.txt","w") as algo:
        for i in range(len(cv)):
            algo.write(f"{Temp[i]} {cv[i]} {Temp[i]-273.15} \n")
    return plt.show()
print(cvt("cobredmt.txt",0.1892329966))
#ncobre=0.1892329966
#nsilicio=0.0612415