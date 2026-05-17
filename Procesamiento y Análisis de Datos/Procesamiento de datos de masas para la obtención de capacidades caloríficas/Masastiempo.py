def masas(nombre):
    nueva=[]
    with open(nombre,"r") as algo:
        for i in algo:
            b=i.strip().split()
            nueva.append(b[0])
    return nueva

def nuevo(archivo,nombrenuevo):
    masa=masas(archivo)
    t=0
    with open(nombrenuevo,"w") as algo:
        for i in range(len(masa)):
            algo.write(f"{masa[i]}" + str(t) + "\n")
            t=t+0.0525

nuevo("cobreambiente.txt","cobreamb")


