import balls

def impData(filename):
    objects=[]
    try:
        with open(filename,'r') as data:
            for line in data:
                x=line.split(';')
                objects.append(balls.Ball(float(x[0]), float(x[1]), [float(x[2]),float(x[3]),float(x[4])], [float(x[5]),float(x[6]),float(x[7])]))
    except FileNotFoundError:
        print("File not found")
    return objects


def expData(filename,objects):
        with open(filename,'w') as data:
            for line in objects:
                data.write(str(line.getMass())+
                           ";"+str(line.getRad())+
                           ";"+str(line.getPos()[0])+
                           ";"+str(line.getPos()[1])+
                           ";"+str(line.getPos()[2])+
                           ";"+str(line.getVel()[0])+
                           ";"+str(line.getVel()[1])+
                           ";"+str(line.getVel()[2])+
                           "\n")

import numpy as np
blist=[]
for _ in range(100):
        m = (np.random.rand() * 100 + 1)*10**11
        r = 1.0
        pos = np.random.rand(3) * 200 - 100
        vel = np.random.rand(3) * 10 - 5
        blist.append(balls.Ball(m, r, pos, vel))

expData("interstellarballs.csv",blist)

a=impData("interstellarballs.csv")
print(a[0].getPos(),4*a[1].getMass())
