Class Particle:
    G = 6.67430e-11
    def __init__(self,  mass, pos, velocity, acc, prev_pos = pos,
     prev_vel = velocity, prev_acc = acc, resolution = 1):
        self.mass = mass #scalor
        self.pos = pos #vector
        self.velocity = velocity #vector
        self.acc = acc #vector

    def momentum(self):
        """calculate the momentum of the particle"""
        return [self.mass*self.velocity[0], self.mass*self.velocity[1]]

    def calcForce(self, other):
        """calculate the gravitation force vector"""
        m1 = self.mass
        m2 = other.mass
        p1 = self.pos
        p2 = other.pos
        r = self.calcDistance(self, other)
        rhat = self.unitVector(self, other)
        FMag = (m1*m2*G)/r**2
        return [FMag*rhat[0], FMag*rhat[1]]

    def calcDistance(self, other):
        """calculate the distance between two objects"""
        return ((self.pos[0] - other.pos[0])**2 + (self.pos[1] - other.pos[1])**2)**0.5

    def unitVector(self, other):
        """calculate unit vector"""
        diff = [self.pos[0] - other.pos[0], self.pos[1] - other.pos[1]]
        mag = calcDistance(self, other)
        return [diff[0]/mag, diff[1]/mag]

    def calcA(self, other):
        F = self.calcForce(self, other)
        return [F[0]/self.mass, F[1]/self.mass]

    def calcV(self):
        pass

    def calcPos(self):
        pass
