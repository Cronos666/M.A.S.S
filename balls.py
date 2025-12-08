import numpy as np

#selfexplanatory
class Ball(object):
    def __init__(self, mass, radius, position, velocity):
        self.m=mass
        self.r=radius
        self.pos=np.array(position)
        self.vel=np.array(velocity)

    #getters
    def getVel(self):
        return self.vel
    
    def getPos(self):
        return self.pos
    
    def getMass(self):
        return self.m
    
    #setters
    def setVel(self,velo):
        self.vel=np.array(velo)
    
    def setPos(self,pos):
        self.pos=pos

#forces calculation 
def forces(list,dt):
    G=1
    flist = []
    for i in list:
        force = np.zeros(3)
        for ii in list:
            if i != ii:
                vecR = list(i).getPos() - list(ii).getPos()
                force += (G*list[i].getMass()*list[ii].getMass()/((np.linalg.norm(vecR))**3))*vecR
        flist.append(force) 

    return flist       




#balls =[]   
#for i in range (10):
#    balls.append(Ball(1,1,(i,i+1,i+2),(1,0,1)))
#balls[0].setVel(np.array((1,2,4)))
#print(balls[0].getVel())
