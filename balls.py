import numpy as np

class Ball(object):
    def __init__(self, mass, radius, position, momentum):
        self.m=mass
        self.r=radius
        self.pos=np.array(position)
        self.mo=np.array(momentum)
        self.vel=self.mo/self.m    

        
c=Ball(2,2,(1,2,3),(4,5,6))
