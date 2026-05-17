def graficar_determinante(M, inicio, fin, n, nombre):
    import numpy as np
    import sympy as sp
    import matplotlib.pyplot as plt
    import csv
    global val
    x = np.arange(inicio, fin, (fin-inicio)/n, dtype=float)
    y = []
    i = 0
    while i < len(x):
        y.append(np.linalg.det(np.array(M.subs(val, x[i]).tolist(), dtype=float)))
        i += 1
    #plt.plot(x, y, color='black')
    #plt.show()
    # cambiar entre 'a' y 'w' si se quiere adjuntar o reescribir
    try:
        # Intenta abrir el archivo en modo de adjuntar (append)
        with open(nombre, mode='a', newline='') as archivo:
            escritor = csv.writer(archivo)
            for fila in zip(x, y):
                escritor.writerow(fila)
    except FileNotFoundError:
        # Si el archivo no existe, crea uno nuevo y escribe los valores
        with open(nombre, mode='w', newline='') as archivo:
            escritor = csv.writer(archivo)
            for fila in zip(x, y):
                escritor.writerow(fila)
    return

###################################################################################################

# HACIENDO VARIAR LOS PARAMETROS

###################################################################################################

import sympy as sp
import numpy as np
val = sp.Symbol('val')

T = 59.782
m = 0.001916
l = 0.226

rep = 10
for j in range(0, 3*rep + 1):
    ln = []
    mn = []
    w2n = []
    w2a = []
    w2d = []
    if j == 0:
        ln = [l,l,l,l,l,l,l,l,l,l,l]
        mn = [m,m,m,m,m,m,m,m,m,m,]
    elif j > 0 and j <= rep:
        ln = [l,l,l,l,l,l,l,l,l,l,l]
        for i in range(0,10):
            mn.append(np.random.normal(m, 0.000012))
    elif j > rep and j <= 2*rep:
        for i in range(0,11):
            ln.append(np.random.normal(l, 0.001))
        mn = [m,m,m,m,m,m,m,m,m,m,]
    else:
        for i in range(0,10):
            ln.append(np.random.normal(l, 0.0015))
            mn.append(np.random.normal(m, 0.000012))
        ln.append(np.random.normal(l, 0.0015))
    i = 0
    while i < 10:
        w2n.append(T*(ln[i]+ln[i+1])/(mn[i]*ln[i]*ln[i+1]))
        if i > 0:
            w2a.append(-T/(mn[i]*ln[i]))
        if i < 9:
            w2d.append(-T/(mn[i]*ln[i+1]))
        i += 1
    n = 2000
    N = sp.Matrix([[w2n[0]-val,w2d[0],0,0,0,0,0,0,0,0],
                    [w2a[0],w2n[1]-val,w2d[1],0,0,0,0,0,0,0],
                    [0,w2a[1],w2n[2]-val,w2d[2],0,0,0,0,0,0],
                    [0,0,w2a[2],w2n[3]-val,w2d[3],0,0,0,0,0],
                    [0,0,0,w2a[3],w2n[4]-val,w2d[4],0,0,0,0],
                    [0,0,0,0,w2a[4],w2n[5]-val,w2d[5],0,0,0],
                    [0,0,0,0,0,w2a[5],w2n[6]-val,w2d[6],0,0],
                    [0,0,0,0,0,0,w2a[6],w2n[7]-val,w2d[7],0],
                    [0,0,0,0,0,0,0,w2a[7],w2n[8]-val,w2d[8]],
                    [0,0,0,0,0,0,0,0,w2a[8],w2n[9]-val]])
    
    limites = [[9000,13000],[42000,46000],[94000,97000],[159000,164000],
                [234000,239000],[313000,318000],[386000,395000],
                [453000,461000],[504000,513000],[536000,546000]]
    # limites = [[0,550000]]

    for i in limites:
        graficar_determinante(N,i[0],i[1],n,'det'+str(j)+'.csv')
        #graficar_determinante(N,i[0],i[1],n,'det00.csv')

################################
# ESTO SIRVE PARA VER LOS P(w) #
################################
        
rep = 10
x = []
y = []
for j in range(0, 3*rep + 1):
#for j in range(0, 3*rep + 2):
    import matplotlib.pyplot as plt
    import csv
    import re
    x.append([])
    y.append([])
    with open('det'+str(j)+'.csv', 'r') as archivo:
    # with open('det'+'0'*(j+1)+'.csv', 'r') as archivo:
        datos = csv.reader(archivo)
        for fila in datos:
            #print(fila, type(fila))
            if fila != []:
                #print(fila, j)
                x[j].append(float(fila[0]))
                y[j].append(float(fila[1]))
    plt.plot(x[j], y[j], label = str(j))
plt.xlabel('w^2')
plt.ylabel('f(w^2)')
plt.title('Masas iguales y distintas')
plt.legend()
plt.show()

#################################################################################################################################

# GRAFICANDO W vs NUMERO DE MODO

#################################################################################################################################

import matplotlib.pyplot as plt
import csv
import math as math

x = []
y = []
ref = []
w = []
wr = []
rep = 10
for i in range(0, 3*rep + 1):
    with open('det'+str(i)+'.csv',"r") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        x.append([])
        y.append([])
        ref.append([])
        w.append([])
        wr.append([])
        for fila in lector:
            x[i].append(float(fila[0]))
            y[i].append(float(fila[1]))
    n = 1
    j = 0
    while j < len(x[i]):
        if j - n*2000 == 0:
            n += 1
        if y[i][j] * y[i][j-1] < 0:
            ref[i].append([])
            ref[i][n-1].append(y[i][j-1])
            ref[i][n-1].append(x[i][j-1])
            ref[i][n-1].append(y[i][j])
            ref[i][n-1].append(x[i][j])
        j += 1
    j = 0
    while j < len(ref[i]):
        w[i].append(math.sqrt(((ref[i][j][0] - ref[i][j][2])*ref[i][j][1]/(ref[i][j][1] - ref[i][j][3]) - ref[i][j][0])/
                    ((ref[i][j][0] - ref[i][j][2])/(ref[i][j][1] - ref[i][j][3])))/(2*math.pi))
        wr[i].append(w[i][j] / w[0][j])
        j += 1
    if i == 0:
        plt.scatter(range(1,len(ref[i]) + 1),w[i], label = "TI")
    elif i > 0 and i <= rep:
        plt.scatter(range(1,len(ref[i]) + 1),w[i], marker='s', label = "MD_LI_"+str(i))
    elif i > rep and i <= 2*rep:
        plt.scatter(range(1,len(ref[i]) + 1),w[i], marker='x', label = "MI_LD_"+str(i-rep))
    else:
        plt.scatter(range(1,len(ref[i]) + 1),w[i], marker='^', label = "MD_LD_"+str(i-2*rep))
    #print(i, w[i])

#plt.plot((1,2,3,4,5,6,7,8,9,10),(22.316,36.151,46.790,62.58,75.05,83.80,99.96,107.3,112.251,117.505),"*",color='black')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

#################################################################################################################################

# DIFERENCIAS PROMEDIO

#################################################################################################################################

wrp = [[],[],[]]
i = 0
while i < len(wr[0]):
    j = 1
    aux = 0
    while j < rep + 1:
        aux += abs(wr[j][i] - wr[0][i])
        j += 1
    wrp[0].append(aux/rep)
    aux = 0
    while j < 2*rep + 1:
        aux += abs(wr[j][i] - wr[0][i])
        j += 1
    wrp[1].append(aux/rep)
    aux = 0
    while j < 3*rep + 1:
        aux += abs(wr[j][i] - wr[0][i])
        j += 1
    wrp[2].append(aux/rep)
    i += 1

import matplotlib.pyplot as plt
for i in range(1, 1 + len(wrp[0])):
    plt.errorbar(i-0.1, wr[0][i-1], yerr=wrp[0][i-1], fmt='o', marker='x', capsize=3, color='darkred')
    plt.errorbar(i, wr[0][i-1], yerr=wrp[1][i-1], fmt='o', marker='s', capsize=3, color='darkblue')
    plt.errorbar(i+0.1, wr[0][i-1], yerr=wrp[2][i-1], fmt='o', marker='^', capsize=3, color='darkgreen')

plt.legend(["Variación de masas","Variación de separaciones","Variación de ambos"])
plt.xlabel('Modo N°', weight='bold')
plt.ylabel('Variación absoluta promedio / w_0', weight='bold', labelpad=15)
plt.show()

# for i in w:
#     print(i)