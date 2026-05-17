import numpy as np
import matplotlib.pyplot as plt
import math
a=4.17
#Recorrido gamma -> X (0,0,0) -> (pi/a ,0 ,0)
Eg=[]
kx=np.linspace(0,2*math.pi/a,1000)
for i in kx:
    Eg.append(-4*(math.cos(i*a/2)*1+1+math.cos(i*a/2)*1))
#Recorrido X -> L (2*pi/a,0,0) -> (pi/a,pi/a,pi/a)
Ex=[]
kyz=np.linspace(0,math.pi/a,1000)
for i in kyz:
    Ex.append(-4*(math.cos((kx[-1]-i)*a/2)*math.cos(i*a/2)+math.cos(i*a/2)*math.cos(i*a/2)+math.cos((kx[-1]-i)*a/2)*math.cos(i*a/2)))

#Recorrido L -> Gamma (pi/a,pi/a,pi/a) -> (0,0,0)
El=[]
for i in kyz:
     El.append(-4*(math.cos((kyz[-1]-i)*a/2)*math.cos((kyz[-1]-i)*a/2)+math.cos((kyz[-1]-i)*a/2)*math.cos((kyz[-1]-i)*a/2)+math.cos((kyz[-1]-i)*a/2)*math.cos((kyz[-1]-i)*a/2)))

gamma=np.linspace(0,math.pi/a,len(Eg))
X=np.linspace(gamma[-1],2*math.pi/a,len(Eg))
L=np.linspace(X[-1],3*math.pi/a,len(Eg))
G2=np.linspace(L[-1],4*math.pi/a,len(Eg))


plt.figure(figsize=(10, 6))

plt.plot(gamma, Eg, label='E(Γ) -> E(X)')
plt.plot(X, Ex, label='E(X) -> E(L)')
plt.plot(L, El, label='E(L) -> E(Γ)')

# Definir las posiciones y etiquetas de las marcas en el eje X
plt.xticks([0, gamma[-1], X[-1], L[-1]], ['Γ', 'X', 'L', 'Γ'])

plt.ylabel('E [eV]')
plt.title('Gráfica de Bandas cualitativas del Au')
plt.legend()
plt.grid(True)
plt.xlim(0,3*math.pi/a)
plt.ylim(-12,4.1)
plt.show()