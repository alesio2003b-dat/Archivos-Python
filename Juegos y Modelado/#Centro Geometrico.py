#Centro Geometrico
def centrogeometrico(nombrearchivo):
    x=[]
    y=[]
    z=[]
    sx=0
    sy=0
    sz=0
    with open(nombrearchivo,"r") as algo:
        for i in algo:
            c=i.split()
            if len(c) ==12 and c[0]=="ATOM" or c[0]=="HETATM":
                print(c)
                x.append(float(c[5]))
                y.append(float(c[6]))
                z.append((float(c[7])))
    for j in x:
        sx=sx+int(j)
    for j in y:
        sy=sy+j
    for j in z:
        sz=sz+j
    return (int(sx/len(x) *1000)/1000.0,int(sy/len(y) *1000)/1000.0,int(sz/len(z) *1000)/1000.0)
print(centrogeometrico("centrogeomet.txt"))
