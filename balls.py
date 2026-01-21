import numpy as np

#selfexplanatory
class Ball(object):
    def __init__(self, mass, radius, position, velocity):
        self.m=mass
        self.r=radius
        self.pos=np.array(position, dtype=float)
        self.vel=np.array(velocity, dtype=float)

    #getters
    def getVel(self):
        return self.vel
    
    def getPos(self):
        return self.pos
    
    def getMass(self):
        return self.m
    
    def getRad(self):
        return self.r

    #setters
    def setVel(self,velo):
        self.vel=np.array(velo, dtype=float)
    
    def setPos(self,pos):
        self.pos=np.array(pos, dtype=float)



#matrix forces calculation
def net_forces(pos, mas, G=6.67428e-11):
#macierz  =pionowy wektor - poziomy wektor 
    d_pos = pos[:,None,:] - pos[None,:,:]
    mM = mas[:,None] * mas[None,:]

    R2 = np.sum(d_pos**2,axis=2)

    #obsluga R=0, wypenia przekatna macierzy ∞ aby dostac 1/R = 0
    np.fill_diagonal(R2,np.inf)

    force = -G*(mM[...,None]*(R2**(-1.5))[...,None]*d_pos)

    return np.sum(force, axis=1)



def dynamics(balls: list[Ball],dt):
    pos = np.array([b.getPos() for b in balls])
    vel = np.array([b.getVel() for b in balls])
    mas = np.array([b.getMass() for b in balls])

    a = net_forces(pos,mas)/mas[:,None]

    new_vel = vel + a*dt
    new_pos = pos + vel*dt

    for i, ball in enumerate(balls):
        ball.setVel(new_vel[i])
        ball.setPos(new_pos[i])

 

def pos_test():
    N=10
    balls = []
    for _ in range(N):
        m = (np.random.rand() * 100 + 1)*10**11
        r = 1.0
        pos = np.random.rand(3) * 200 - 100
        vel = np.random.rand(3) * 10 - 5
        balls.append(Ball(m, r, pos, vel))

    for ball in balls:
        print(ball.getPos())

    dynamics(balls,0.1)
    print("="*42)
    for ball in balls:
        print(ball.getPos())

