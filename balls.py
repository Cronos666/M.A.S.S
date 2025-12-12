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
    
    #setters
    def setVel(self,velo):
        self.vel=np.array(velo, dtype=float)
    
    def setPos(self,pos):
        self.pos=np.array(pos, dtype=float)

#iterational forces calculation 
def net_forces(balls: list[Ball], G=6.67428e-11):
    N=len(balls)
    flist = [np.zeros(3) for n in range(N)]
    for i in range(N):
        ball_i = balls[i]
        for ii in range(i+1,N):
            ball_ii = balls[ii]
            
            vecR = ball_i.getPos() - ball_ii.getPos()
            R2 = np.dot(vecR,vecR)
            if R2 == 0:
                continue
 
            force = (-1)*(G*ball_i.getMass()*ball_ii.getMass()/(R2*np.sqrt(R2)))*vecR
 
            flist[i] += force
            flist[ii] -= force
 
    return flist       


#matrix forces calculation
def net_forces_fast(pos, mas, G=6.67428e-11):
#macierz  =pionowy wektor - poziomy wektor 
    d_pos = pos[:,None,:] - pos[None,:,:]

    mM = mas[:,None] * mas[None,:]

    R2 = np.sum(d_pos**2,axis=2)

    #obsluga R=0, wypenia przekatna macierzy ∞ aby dostac 1/R = 0
    np.fill_diagonal(R2,np.inf)

    force = -G*(mM[...,None]*(R2**(-1.5))[...,None]*d_pos)

    return np.sum(force, axis=1)






def speedtest():
    N=1000
    balls = []
    for _ in range(N):
        m = (np.random.rand() * 100 + 1)*10**11
        r = 1.0
        pos = np.random.rand(3) * 200 - 100
        vel = np.random.rand(3) * 10 - 5
        balls.append(Ball(m, r, pos, vel))



    import time
    start_time = time.time()
    forces_old = net_forces(balls)
    end_time = time.time()
    time_old = end_time - start_time

    start_prep = time.time()
    pos_array = np.array([b.getPos() for b in balls])
    mass_array = np.array([b.getMass() for b in balls])
    prep_time = time.time() - start_prep

    start_time = time.time()
    forces_new = net_forces_fast(pos_array, mass_array)
    end_time = time.time()
    time_new = end_time - start_time

    print("Iterational:",time_old)
    print("Prep:",prep_time)
    print("Matrix:",time_new)


speedtest();
